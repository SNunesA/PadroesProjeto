class Usuario:
    def __init__(self):
        #usuario padrao
        self.editar_perfil=False
        self.resetar_senha=False
        self.cadastrar_empresa=False
        
        #admin
        self.remover_usuario=False
        self.editar_usuario=False
        self.remover_empresa=False
        self.resetar_senhausuarios=False
        
    def __repr__(self):
        atributos_true = [
            ("Editar perfil", self.editar_perfil),
            ("Cadastrar empresa", self.cadastrar_empresa),
            ("Resetar senha", self.resetar_senha),
            ("Remover usuário", self.remover_usuario),
            ("Editar usuário", self.editar_usuario),
            ("Remover empresa", self.remover_empresa),
            ("Resetar senha usuários", self.resetar_senhausuarios),
        ]

        linhas = [f"Usuário: {id(self)}"]
        for nome, valor in atributos_true:
            if valor:
                linhas.append(f"{nome}: {valor}")

        return "\n".join(linhas)
 
        
class UsuarioPadraoBuilder:
    def __init__(self):
        self.usuario = Usuario()
    
    def set_editar_perfil(self, editar_perfil: bool):
        self.usuario.editar_perfil = editar_perfil
        return self

    def set_resetar_senha(self, resetar_senha: bool):
        self.usuario.resetar_senha = resetar_senha
        return self

    def set_cadastrar_empresa(self, cadastrar_empresa: bool):
        self.usuario.cadastrar_empresa = cadastrar_empresa
        return self
    
    def build(self) -> Usuario:
        return self.usuario
    
class UsuarioAdminBuilder:
    def __init__(self):
        self.usuario = Usuario()
    
    def set_remover_usuario(self, remover_usuario: bool):
        self.usuario.remover_usuario = remover_usuario
        return self

    def set_editar_usuario(self, editar_usuario: bool):
        self.usuario.editar_usuario = editar_usuario
        return self

    def set_cadastrar_empresa(self, cadastrar_empresa: bool):
        self.usuario.cadastrar_empresa = cadastrar_empresa
        return self

    def set_remover_empresa(self, remover_empresa: bool):
        self.usuario.remover_empresa = remover_empresa
        return self

    def set_resetar_senhausuarios(self, resetar_senhausuarios: bool):
        self.usuario.resetar_senhausuarios = resetar_senhausuarios
        return self
    
    def build(self) -> Usuario:
        return self.usuario
    

if __name__ == "__main__":
    print()
    stefhany=(UsuarioPadraoBuilder()
              .set_editar_perfil(True)
              .set_cadastrar_empresa(True)
              .set_resetar_senha(True)
              .build()
              )
    print(stefhany)
    print()
    ifpr=(UsuarioAdminBuilder()
          .set_remover_usuario(True)
          .set_editar_usuario(True)
          .set_cadastrar_empresa(True)
          .set_remover_empresa(True)
          .set_resetar_senhausuarios(True)
          .build()
          )
    print(ifpr)
    print()