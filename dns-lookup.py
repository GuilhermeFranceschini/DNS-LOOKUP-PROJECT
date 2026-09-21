import dns.resolver
domain = input("Digite o domínio que deseja consultar: ")
def dnslook(domain, record_type):
    answers = dns.resolver.resolve(domain, 'A')
    for answer in answers:
        print(f"Endereço IP: {answer.to_text()}")
dnslook(domain, 'A')
dnslook(domain, 'AAAA')
dnslook(domain, 'MX')
dnslook(domain, 'NS')


