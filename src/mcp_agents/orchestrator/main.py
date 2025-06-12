from loguru import logger
import yaml

from src.mcp_agents.agents.finops_agent.model import FinOpsModel
from src.mcp_agents.agents.finops_agent.context import FinOpsContext
from src.mcp_agents.agents.finops_agent.protocol import FinOpsProtocol

from src.mcp_agents.agents.governanca_agent.model import GovernancaModel
from src.mcp_agents.agents.governanca_agent.context import GovernancaContext
from src.mcp_agents.agents.governanca_agent.protocol import GovernancaProtocol

from src.mcp_agents.agents.pipeline_agent.model import PipelineModel
from src.mcp_agents.agents.pipeline_agent.context import PipelineContext
from src.mcp_agents.agents.pipeline_agent.protocol import PipelineProtocol

from src.mcp_agents.agents.mlops_agent.model import MLOpsModel
from src.mcp_agents.agents.mlops_agent.context import MLOpsContext
from src.mcp_agents.agents.mlops_agent.protocol import MLOpsProtocol

from src.mcp_agents.agents.dashboards_agent.model import DashModel
from src.mcp_agents.agents.dashboards_agent.context import DashContext
from src.mcp_agents.agents.dashboards_agent.protocol import DashProtocol


def main():
    logger.add("logs/execucao.log", rotation="1 MB", level="INFO")

    # FinOps
    billing_data = {"bigquery": 1200, "dataflow": 200, "vertex_ai": 800}
    f_model = FinOpsModel()
    f_context = FinOpsContext(billing_data)
    f_protocol = FinOpsProtocol()
    f_protocol.notify(f_model.check_cost(f_context.billing_data))

    # Governança
    metadados = ["cpf_cliente", "nome", "email_contato"]
    g_model = GovernancaModel()
    g_context = GovernancaContext(metadados)
    g_protocol = GovernancaProtocol()
    g_protocol.alertar(g_model.verificar_pii(g_context.metadados))

    # Pipelines
    execucoes = {"dag_clientes": "SUCCESS", "dag_fraudes": "FAILED"}
    p_model = PipelineModel()
    p_context = PipelineContext(execucoes)
    p_protocol = PipelineProtocol()
    p_protocol.emitir_alertas(p_model.detectar_falhas(p_context.historico))

    # MLOps
    metricas = {"drift_score": 0.45}
    m_model = MLOpsModel()
    m_context = MLOpsContext(metricas)
    m_protocol = MLOpsProtocol()
    if m_model.detectar_drift(m_context.metricas):
        m_protocol.acionar_retreinamento()

    # Dashboards
    acessos = {"lucro_liquido": 40, "KPI_inativo": 0}
    d_model = DashModel()
    d_context = DashContext(acessos)
    d_protocol = DashProtocol()
    d_protocol.sugerir_remocao(d_model.detectar_kpi_obsoleto(d_context.acessos))

    # Governança - Data Contracts
    try:
        with open("data/contract_cedente.yaml", "r") as file:
            contrato_yaml = yaml.safe_load(file)
    except FileNotFoundError:
        logger.error("[GOV] Arquivo de contrato não encontrado!")
        contrato_yaml = {}

    entrada = {"cpf": 12345678900, "score": 720, "tempoRelacionamento": 3.5}

    if contrato_yaml:
        erros = g_model.validar_contrato(entrada, contrato_yaml)
        if erros:
            logger.warning("[GOV] Erros de validação do contrato:")
            for erro in erros:
                logger.warning(f" - {erro}")
        else:
            logger.info("[GOV] Dados válidos segundo o contrato.")


if __name__ == "__main__":
    main()
