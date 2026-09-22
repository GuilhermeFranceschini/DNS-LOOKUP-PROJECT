import dns.resolver
def dnslook(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        for answer in answers:
            print(f"{record_type}: {answer.to_text()}")
    except dns.resolver.NXDOMAIN:
        print(f"{record_type}: Domínio não encontrado.")
    except dns.resolver.NoAnswer:
        print(f"{record_type}: Nenhum registro encontrado.")    
print("Bem-vindo ao programa de consulta DNS!\n")
domain = input("Digite o domínio que deseja consultar: ")
if not domain:
    print("Nenhum domínio fornecido. Encerrando o programa.")
    exit()
print("\nn1. Consultar registros A (IPv4)" \
"\nn2. Consultar registros AAAA (IPv6)" \
"\nn3. Consultar registros MX (Mail Exchange)" \
"\nn4. Consultar registros NS (Name Server)")
opcao = int(input("\nDigite o número da opção desejada: "))
if opcao == 1:
    dnslook(domain, 'A')
if opcao == 2:
    dnslook(domain, 'AAAA')
if opcao == 3:
    dnslook(domain, 'MX')
if opcao == 4:
    dnslook(domain, 'NS')
if opcao < 1 or opcao > 4:
    print("Opção inválida. Encerrando o programa.")
print("Consulta concluída.\n")

