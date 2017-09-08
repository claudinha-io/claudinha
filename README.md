# claudinha
Script de Ansible para provisionar experimentos com uma pequena nuvem com Raspberry Pi e Unicorn Hat

@TODO

- Testes de Infraestrutura
- Provisionamento de multiplos ambientes
- Proxy Reverso
- Incluir Agente do Travis


## Comandos de Ansible

### Deploy
`python3 /usr/bin/ansible-playbook -D -i hosts playbook.yml --ask-vault-pass`

### Test
`ansible-playbook -C -D -i hosts playbook.yml --ask-vault-pass`

## Comandos via browser

### Mostrar um Hello, World! no browser
`http://ip_ou_dns_do_host/`

### Mostrar a hora no UH e no Browser
`http://ip_ou_dns_do_host/message`

### Mostrar um texto no UH e no Browser
`http://ip_ou_dns_do_host/message/<texto>`

### Mostrar um texto com cor especifica no UH e no Browser

`http://ip_ou_dns_do_host/message/<texto>?color=<cor>`

- white => rgb(255, 255, 255) => #FFFFFF
- red => rgb(255, 0, 0) => #FF0000
- green => rgb(0, 255, 0) => #00FF00
- blue => rgb(0, 0, 255) => #0000FF
- yellow => rgb(255, 255, 0) => #FFFF00
- cyan => rgb(0, 255, 255) => #00FFFF
- magenta => rgb(255, 0, 255) => #FF00FF
