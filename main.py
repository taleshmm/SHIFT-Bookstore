from service.category_service import CategoryService

category_service = CategoryService()

def principal_menu():
     print('''\n[Menu Principal] Escolha uma das seguintes opções:
  1 - Categorias
  0 - Sair do programa''')
     selection = input('Digite a opção: ')
     
     if selection == '0':
        print('Obrigado, até logo!')
        return
     if selection == '1':
        category_service.menu()
     else:
        print('Opção inválida! Por favor, tente novamente!')
     
     principal_menu() 

if __name__ == '__main__':
    print('Bem-vindo a Livraria SHIFT - Mastering Python!')
    principal_menu()


      
