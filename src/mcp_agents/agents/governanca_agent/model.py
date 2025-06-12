class GovernancaModel:
    def verificar_pii(self, metadados):
        return [campo for campo in metadados if "cpf" in campo or "email" in campo]

    def validar_contrato(self, dados, contrato):
        erros = []
        for campo in contrato.get("fields", []):
            nome = campo["name"]
            tipo = campo["type"]
            obrigatorio = campo.get("required", False)
            if obrigatorio and nome not in dados:
                erros.append(f"Campo obrigatório ausente: {nome}")
                continue
            if nome in dados:
                valor = dados[nome]
                if tipo == "string" and not isinstance(valor, str):
                    erros.append(f"Tipo incorreto para {nome}, esperado string")
                elif tipo == "integer" and not isinstance(valor, int):
                    erros.append(f"Tipo incorreto para {nome}, esperado integer")
                elif tipo == "float" and not isinstance(valor, float):
                    erros.append(f"Tipo incorreto para {nome}, esperado float")
        return erros
