from .user import UserRegistrationSerializer, UserSerializer
from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .livro import LivroListSerializer, LivroRetrieveSerializer, LivroSerializer
from .compra import (
    CompraCreateUpdateSerializer,
    CompraListSerializer, # novo
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer, # novo
    ItensCompraSerializer,
)