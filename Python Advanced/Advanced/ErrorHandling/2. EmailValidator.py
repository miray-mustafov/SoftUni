class NameTooShort(Exception):
    pass
class MustContainAtSymbolError(Exception):
    pass
class InvalidDomainError(Exception):
    pass

extensions=['.com', '.bg', '.org', '.net']
email=input()


def is_valid_domain(domain, extensions):
    for ext in extensions:
        if domain.endswith(ext):
            return True
    return False


while email:
    if not email.count('@')==1:
        raise MustContainAtSymbolError("Email must contain 1 @")

    username, domain = email.split('@')
    if len(username) <= 4:
        raise NameTooShort("Name must be more than 4 characters")

    if not is_valid_domain(domain,extensions):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email=input()