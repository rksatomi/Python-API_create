from typing import Annotated
from pydantic import Field
from workoutapi.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do Centro de Treinamento', example='Rua x, Q2', max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do proprietario ', example='Carlos Magno', max_length=30)]