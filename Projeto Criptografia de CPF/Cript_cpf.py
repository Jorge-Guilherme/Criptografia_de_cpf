# PROGRAMA DE CRIPTOGRAFIA DE DADOS
cpf= ''
output_cpf = []
cript = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
while True:
    cpf_input = input('Digite seu CPF: ')
    for sep in cpf_input:
        if sep.isnumeric(): cpf += sep
    conditions = cpf.isnumeric() and len(cpf) == 11
    if conditions: break
    else: print('Você não digitou um CPF válido')
    
for iter in cpf: output_cpf.append(cript[int(iter)])
print(output_cpf)
