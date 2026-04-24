# Network Enumeration Tool

Ferramenta em Python para enumeração de rede local, combinando:

- Port scanning (TCP)
- Identificação de serviços HTTP
- Salvamento de resultados em JSON

## Objetivo

Projeto educacional focado em:
- fundamentos de redes (IP, portas)
- uso de sockets (baixo nível)
- requisições HTTP
- integração de múltiplas etapas de enumeração

## Funcionalidades

- Varredura de IPs em rede local (/24)
- Scan de múltiplas portas TCP
- Identificação de portas abertas
- Análise HTTP automática (status + servidor)
- Execução concorrente (threads)
- Salvamento de resultados em arquivo JSON

## Estrutura do Projeto

- `main.py` → código principal
- `results.json` → saída gerada automaticamente

## Configuração

Edite no topo do código:

```python
BASE_IP = "192.168.0"
PORTS = [21, 22, 23, 53, 80, 443, 8080, 7547]
TIMEOUT = 1
MAX_THREADS = 100
HTTP_TIMEOUT = 3

Como usar
Descubra seu IP local (ex: 192.168.1.23)
Ajuste o BASE_IP (ex: 192.168.1)
Execute: python main.py
Exemplo de saída (terminal)
[HOST] 192.168.0.1 -> [80, 443]
Exemplo de saída (JSON)
{
  "192.168.0.1": {
    "ports": [80, 443],
    "http": [
      {
        "url": "http://192.168.0.1:80",
        "status": 200,
        "server": "nginx"
      }
    ]
  }
}

Limitações
Não detecta hosts sem portas abertas
Pode gerar falsos negativos (timeout/firewall)
Não realiza scan completo de portas
Não utiliza ICMP (ping)
Não substitui ferramentas profissionais
Aviso legal

Uso estritamente educacional.
Não utilize em redes sem autorização.

Próximas melhorias
CLI com argumentos (argparse)
Scan de range de portas completo
Exportação em CSV
Detecção de serviços mais avançada
Melhor paralelismo
Autor

Projeto desenvolvido para estudo prático de redes e cibersegurança.
