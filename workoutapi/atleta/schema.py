from pydantic import Field, PositiveFloat
from typing import Annotated
from workoutapi.contrib.schemas import BaseSchema


class Ateta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=25.5)]
    altura: Annotated[PositiveFloat, Field(description='altura do atleta', example=1.25)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]