import dns.resolver
def dnslook(domain, record_type):
    domain = input("Digite o domínio que deseja consultar: ")
    answers = dns.resolver.resolve(domain, 'A')
    for answer in answers:
        print(f"Endereço IP: {answer.to_text()}")
dnslook('example.com', 'A')

