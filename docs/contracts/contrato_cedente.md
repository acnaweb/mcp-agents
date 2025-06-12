# 📜 Documentação de Data Contract: contrato_cedente_v1

**Descrição:** Schema e regras do dado de entrada do cedente  
**Versão:** 1  
**Responsável:** dados.riscos@banco.com

---

## 🧾 Campos

| Campo               | Tipo     | Obrigatório | PII  | Validação Extra         |
|---------------------|----------|-------------|------|--------------------------|
| `cpf`               | string   | ✅           | ✅   | CPF com 11 dígitos       |
| `score`             | integer  | ❌           | ❌   | 0 <= score <= 1000       |
| `tempoRelacionamento` | float | ❌           | ❌   |                          |

---

## 🔍 Validadores

1. `valida_score_minimo`: `score >= 500`  
2. `valida_cpf_valido`: `len(cpf) == 11 and cpf.isdigit()`

---

## ✅ Exemplo de entrada válida

```json
{
  "cpf": "12345678900",
  "score": 800,
  "tempoRelacionamento": 2.5
}
```

## ❌ Exemplo de entrada inválida

```json
{
  "cpf": 12345678900,
  "score": "alto"
}
```
