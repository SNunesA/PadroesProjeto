## Padroes de Projeto Utilizados: 
### 1. **Abstract Factory**
📁 Arquivo abstractfactory.py

Responsável por **criar famílias de NPCs** com diferentes elementos (ex: fogo, água), sem depender das classes concretas.

- A `AbstractFactory` define a interface `createNPC`.
- As classes `FogoFactory` e `AguaFactory` implementam essa interface e instanciam os inimigos corretos.


### 2. **Decorator**
📁 Arquivo decoratorequip.py

Usado para **equipar o jogador dinamicamente com poções** que aumentam atributos como vida, ataque ou defesa, sem alterar a classe base `Player`.

- `EquipamentoDecorator` encapsula um `Player`.
- Subclasses como `Vida`, `Ataque` e `Defesa` aumentam atributos.

### 3. **State**
📁 Arquivo state.py

Controla **o comportamento do jogador de acordo com seu estado de saúde**.

- `Saudavel` e `EmChamas` são estados que afetam `atacar()` e `defender()`.
- O jogador muda de estado ao sofrer certos ataques, como "Ataque Meteoro".

### 4. **Chain of Responsibility**
📁 Arquivo chainresponsability.py

Define uma cadeia de decisão para **determinar qual tipo de ataque o NPC irá usar**.

- Handlers como `FogoHandler`, `AguaHandler` e `NormalHandler` decidem se executam ou passam o ataque para o próximo da cadeia.

### 5. **Builder**
📁 Arquivo builder.py

Usado para **construir objetos `Player` com atributos personalizados** (nome, vida, ataque, defesa, kits...).

- A classe `PlayerBuilder` possui métodos encadeáveis como `.set_nome()`, `.set_saude()`, etc.
- O método `build()` retorna um `Player` configurado com estado e atributos.

