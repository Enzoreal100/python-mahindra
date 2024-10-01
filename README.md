# Descrição do Projeto

**TechAdvanced** é uma plataforma interativa para a compra e gestão de NFTs (Tokens Não Fungíveis) relacionadas a equipes em competições. O sistema permite que usuários se cadastrem, façam login, comprem NFTs, visualizem suas compras e gerenciem suas carteiras. Além disso, administradores têm a capacidade de alterar as posições das equipes, o que impacta diretamente nos preços das NFTs.
Utilizamos a biblioteca pyfiglet para a adição de uma arte ASCII, é importante tê-la para o funcionamento do código

## Funcionalidades Principais

1. **Login e Cadastro**:
   - Usuários podem se cadastrar e realizar login.
   - Administradores têm uma área específica de login.

2. **Navegação do Usuário**:
   - Visualização de preços de NFTs.
   - Visualização de posições das equipes.
   - Compra de NFTs e visualização do carrinho.
   - Exibição das NFTs que o usuário possui.

3. **Administração**:
   - Alteração de posições das equipes.
   - Ajuste automático dos preços das NFTs baseado na nova posição.

## Diagrama em Blocos

```plaintext
+---------------------+
|   Início do Sistema |
+---------------------+
          |
          v
+---------------------+
|  Escolha de Ação    |
|  (Login/Cadastro)   |
+---------------------+
          |
          +-----------------------------------+
          |                                   |
          v                                   v
+---------------------+               +---------------------+
|  Login como Usuário |               |  Login como Admin   |
+---------------------+               +---------------------+
          |                                   |
          v                                   v
+---------------------+               +---------------------+
|  Menu do Usuário    |               |  Menu do Admin      |
+---------------------+               +---------------------+
          |                                   |
+---------+-----------+               +-------+---------+
|   1. Ver Preços     |               |  1. Alterar      |
|   2. Ver Posições   |               |     Posições     |
|   3. Comprar NFTs   |               |  2. Sair         |
|   4. Exibir Carrinho|               +-------------------+
|   5. Exibir NFTs    |
|   6. Sair           |
+---------------------+
          |
          v
+---------------------+
|   Carrinho de Compras|
+---------------------+
          |
          v
+---------------------+
|   Confirmação de    |
|   Compra e Saldo    |
+---------------------+
          |
          v
+---------------------+
|    Fim do Sistema    |
+---------------------+
```
# Funcionamento do Código

## Início do Sistema
O usuário é apresentado com opções para logar, cadastrar ou sair.

## Login
Se o usuário escolhe fazer login, ele insere seu nome de usuário e senha, que são verificados.

## Menu do Usuário
O usuário tem acesso a um menu onde pode escolher entre diferentes ações relacionadas às NFTs.

### Compra de NFTs
Se o usuário optar por comprar NFTs, ele pode adicionar NFTs ao carrinho e visualizar o total antes de finalizar a compra.

## Administração
Os administradores podem alterar a posição das equipes, afetando os preços das NFTs.

## Finalização
O usuário ou administrador pode sair do sistema, encerrando a sessão.

## Conclusão
O projeto **TechAdvanced** proporciona uma experiência interativa para usuários e administradores, permitindo a gestão de NFTs de maneira intuitiva e dinâmica. As funções de verificação e manipulação de dados garantem que as interações sejam seguras e precisas.

