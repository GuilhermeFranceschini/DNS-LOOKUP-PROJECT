import dns.resolver
print("Bem-vindo ao programa de consulta DNS!\n")
domain = input("Digite o domínio que deseja consultar: ")
def dnslook(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        for answer in answers:
            print(f"Resultado: {answer.to_text()}")
    except dns.resolver.NXDOMAIN:
        print(f"{record_type}: Domínio não encontrado.")
    except dns.resolver.NoAnswer:
        print(f"{record_type}: Nenhum registro encontrado.")
    print("Consulta concluída.\n")

dnslook(domain, 'A')
dnslook(domain, 'AAAA')
dnslook(domain, 'MX')
dnslook(domain, 'NS')


