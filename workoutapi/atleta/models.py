from datetime import datetime
from sqlalchemy import ForeignKey, Integer, DateTime, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workoutapi.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = "atleta"
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[int] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categoria.pk_id'))
    cetro_treinamento: Mapped['Centro Treinamento'] = relationship(back_populates='atleta')
    cetro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('cetro_treinamento .pk_id'))
