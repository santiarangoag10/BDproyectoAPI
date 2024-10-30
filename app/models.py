from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime
from typing import Optional

class SedeCreate(BaseModel):
    nombre: str = Field(..., description="Nombre de la sede (campo requerido)")
    direccion: Optional[str] = Field(None, description="Dirección de la sede")
    telefono: Optional[str] = Field(None, description="Teléfono de la sede")

class Sede(SedeCreate):
    sede_id: int

class ClienteCreate(BaseModel):
    nombre: str = Field(..., description="Nombre del cliente (campo requerido)")
    email: EmailStr = Field(..., description="Correo electrónico del cliente (campo requerido)")
    telefono: Optional[str] = Field(None, description="Teléfono del cliente")
    direccion: Optional[str] = Field(None, description="Dirección del cliente")
    fecha_registro: Optional[date] = Field(default=None, description="Fecha de registro del cliente")

class Cliente(ClienteCreate):
    cliente_id: int

class EmpleadoCreate(BaseModel):
    nombre: str = Field(..., description="Nombre del empleado (campo requerido)")
    cargo: Optional[str] = Field(None, description="Cargo del empleado")
    telefono: Optional[str] = Field(None, description="Teléfono del empleado")
    email: Optional[EmailStr] = Field(None, description="Correo electrónico del empleado")
    sede_id: Optional[int] = Field(None, description="ID de la sede donde trabaja el empleado")

class Empleado(EmpleadoCreate):
    empleado_id: int

class ProveedorCreate(BaseModel):
    nombre: str = Field(..., description="Nombre del proveedor (campo requerido)")
    contacto: Optional[str] = Field(None, description="Nombre del contacto del proveedor")
    telefono: Optional[str] = Field(None, description="Teléfono del proveedor")
    direccion: Optional[str] = Field(None, description="Dirección del proveedor")

class Proveedor(ProveedorCreate):
    proveedor_id: int

class ProductoCreate(BaseModel):
    nombre: str = Field(..., description="Nombre del producto (campo requerido)")
    descripcion: Optional[str] = Field(None, description="Descripción del producto")
    precio: float = Field(..., description="Precio del producto (campo requerido)")
    stock: Optional[int] = Field(default=0, description="Stock disponible del producto")
    proveedor_id: Optional[int] = Field(None, description="ID del proveedor del producto")

class Producto(ProductoCreate):
    producto_id: int

class FacturacionCreate(BaseModel):
    cliente_id: Optional[int] = Field(None, description="ID del cliente")
    empleado_id: Optional[int] = Field(None, description="ID del empleado")
    fecha_factura: Optional[datetime] = Field(default=None, description="Fecha y hora de la factura")
    total: float = Field(..., description="Total de la factura (campo requerido)")

class Facturacion(FacturacionCreate):
    factura_id: int