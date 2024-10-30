from fastapi import APIRouter, HTTPException
from app.models import (SedeCreate, Sede, ClienteCreate, Cliente, 
                       EmpleadoCreate, Empleado, ProveedorCreate, Proveedor,
                       ProductoCreate, Producto, FacturacionCreate, Facturacion)
from app.database import get_db_connection
from typing import List

router = APIRouter()

# Endpoints para Sedes
@router.post("/sedes/", response_model=Sede, tags=["Sedes"])
def crear_sede(sede: SedeCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO Sedes (nombre, direccion, telefono)
        VALUES (%s, %s, %s)
        """
        values = (sede.nombre, sede.direccion, sede.telefono)
        cursor.execute(query, values)
        conn.commit()
        sede_id = cursor.lastrowid
        return Sede(sede_id=sede_id, **sede.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/sedes/", response_model=List[Sede], tags=["Sedes"])
def listar_sedes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Sedes")
        sedes = cursor.fetchall()
        return [Sede(**sede) for sede in sedes]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/sedes/bulk/", response_model=List[Sede], tags=["Sedes"])
def crear_sedes_bulk(sedes: List[SedeCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        created_sedes = []
        for sede in sedes:
            query = """
            INSERT INTO Sedes (nombre, direccion, telefono)
            VALUES (%s, %s, %s)
            """
            values = (sede.nombre, sede.direccion, sede.telefono)
            cursor.execute(query, values)
            sede_id = cursor.lastrowid
            created_sedes.append(Sede(sede_id=sede_id, **sede.dict()))
        conn.commit()
        return created_sedes
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Endpoints para Clientes
@router.post("/clientes/", response_model=Cliente, tags=["Clientes"])
def crear_cliente(cliente: ClienteCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO Clientes (nombre, email, telefono, direccion, fecha_registro)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (cliente.nombre, cliente.email, cliente.telefono, 
                 cliente.direccion, cliente.fecha_registro)
        cursor.execute(query, values)
        conn.commit()
        cliente_id = cursor.lastrowid
        return Cliente(cliente_id=cliente_id, **cliente.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/clientes/", response_model=List[Cliente], tags=["Clientes"])
def listar_clientes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Clientes")
        clientes = cursor.fetchall()
        return [Cliente(**cliente) for cliente in clientes]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/clientes/bulk/", response_model=List[Cliente], tags=["Clientes"])
def crear_clientes_bulk(clientes: List[ClienteCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        created_clientes = []
        for cliente in clientes:
            query = """
            INSERT INTO Clientes (nombre, email, telefono, direccion, fecha_registro)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (cliente.nombre, cliente.email, cliente.telefono,
                     cliente.direccion, cliente.fecha_registro)
            cursor.execute(query, values)
            cliente_id = cursor.lastrowid
            created_clientes.append(Cliente(cliente_id=cliente_id, **cliente.dict()))
        conn.commit()
        return created_clientes
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Endpoints para Empleados
@router.post("/empleados/", response_model=Empleado, tags=["Empleados"])
def crear_empleado(empleado: EmpleadoCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO Empleados (nombre, cargo, telefono, email, sede_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (empleado.nombre, empleado.cargo, empleado.telefono,
                 empleado.email, empleado.sede_id)
        cursor.execute(query, values)
        conn.commit()
        empleado_id = cursor.lastrowid
        return Empleado(empleado_id=empleado_id, **empleado.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/empleados/", response_model=List[Empleado], tags=["Empleados"])
def listar_empleados():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Empleados")
        empleados = cursor.fetchall()
        return [Empleado(**empleado) for empleado in empleados]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/empleados/bulk/", response_model=List[Empleado], tags=["Empleados"])
def crear_empleados_bulk(empleados: List[EmpleadoCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        created_empleados = []
        for empleado in empleados:
            query = """
            INSERT INTO Empleados (nombre, cargo, telefono, email, sede_id)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (empleado.nombre, empleado.cargo, empleado.telefono,
                     empleado.email, empleado.sede_id)
            cursor.execute(query, values)
            empleado_id = cursor.lastrowid
            created_empleados.append(Empleado(empleado_id=empleado_id, **empleado.dict()))
        conn.commit()
        return created_empleados
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Endpoints para Proveedores
@router.post("/proveedores/", response_model=Proveedor, tags=["Proveedores"])
def crear_proveedor(proveedor: ProveedorCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO Proveedores (nombre, contacto, telefono, direccion)
        VALUES (%s, %s, %s, %s)
        """
        values = (proveedor.nombre, proveedor.contacto, proveedor.telefono,
                 proveedor.direccion)
        cursor.execute(query, values)
        conn.commit()
        proveedor_id = cursor.lastrowid
        return Proveedor(proveedor_id=proveedor_id, **proveedor.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/proveedores/", response_model=List[Proveedor], tags=["Proveedores"])
def listar_proveedores():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Proveedores")
        proveedores = cursor.fetchall()
        return [Proveedor(**proveedor) for proveedor in proveedores]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/proveedores/bulk/", response_model=List[Proveedor], tags=["Proveedores"])
def crear_proveedores_bulk(proveedores: List[ProveedorCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        created_proveedores = []
        for proveedor in proveedores:
            query = """
            INSERT INTO Proveedores (nombre, contacto, telefono, direccion)
            VALUES (%s, %s, %s, %s)
            """
            values = (proveedor.nombre, proveedor.contacto, proveedor.telefono,
                     proveedor.direccion)
            cursor.execute(query, values)
            proveedor_id = cursor.lastrowid
            created_proveedores.append(Proveedor(proveedor_id=proveedor_id, **proveedor.dict()))
        conn.commit()
        return created_proveedores
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Endpoints para Productos
@router.post("/productos/", response_model=Producto, tags=["Productos"])
def crear_producto(producto: ProductoCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO Productos (nombre, descripcion, precio, stock, proveedor_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (producto.nombre, producto.descripcion, producto.precio,
                 producto.stock, producto.proveedor_id)
        cursor.execute(query, values)
        conn.commit()
        producto_id = cursor.lastrowid
        return Producto(producto_id=producto_id, **producto.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/productos/", response_model=List[Producto], tags=["Productos"])
def listar_productos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Productos")
        productos = cursor.fetchall()
        return [Producto(**producto) for producto in productos]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/productos/bulk/", response_model=List[Producto], tags=["Productos"])
def crear_productos_bulk(productos: List[ProductoCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        created_productos = []
        for producto in productos:
            query = """
            INSERT INTO Productos (nombre, descripcion, precio, stock, proveedor_id)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (producto.nombre, producto.descripcion, producto.precio,
                     producto.stock, producto.proveedor_id)
            cursor.execute(query, values)
            producto_id = cursor.lastrowid
            created_productos.append(Producto(producto_id=producto_id, **producto.dict()))
        conn.commit()
        return created_productos
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Endpoints para Facturación
@router.post("/facturacion/", response_model=Facturacion, tags=["Facturacion"])
def crear_factura(factura: FacturacionCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO Facturacion (cliente_id, empleado_id, fecha_factura, total)
        VALUES (%s, %s, %s, %s)
        """
        values = (factura.cliente_id, factura.empleado_id,
                 factura.fecha_factura, factura.total)
        cursor.execute(query, values)
        conn.commit()
        factura_id = cursor.lastrowid
        return Facturacion(factura_id=factura_id, **factura.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/facturacion/", response_model=List[Facturacion], tags=["Facturacion"])
def listar_facturas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Facturacion")
        facturas = cursor.fetchall()
        return [Facturacion(**factura) for factura in facturas]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/facturacion/bulk/", response_model=List[Facturacion], tags=["Facturacion"])
def crear_facturas_bulk(facturas: List[FacturacionCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        created_facturas = []
        for factura in facturas:
            query = """
            INSERT INTO Facturacion (cliente_id, empleado_id, fecha_factura, total)
            VALUES (%s, %s, %s, %s)
            """
            values = (factura.cliente_id, factura.empleado_id,
                     factura.fecha_factura, factura.total)
            cursor.execute(query, values)
            factura_id = cursor.lastrowid
            created_facturas.append(Facturacion(factura_id=factura_id, **factura.dict()))
        conn.commit()
        return created_facturas
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# query

@router.get("/query1/", tags=["Query1 getproducts"])
def getproducts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Productos")
        productos = cursor.fetchall()
        return [Producto(**producto) for producto in productos]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/query2/", tags=["query2 productos por proveedor"])
def productos_por_proveedor():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT 
            p.nombre as proveedor,
            COUNT(pr.producto_id) as total_productos,
            AVG(pr.precio) as precio_promedio
        FROM Proveedores p
        LEFT JOIN Productos pr ON p.proveedor_id = pr.proveedor_id
        GROUP BY p.proveedor_id, p.nombre
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

@router.get("/query3/", tags=["query3 empleados por sede y facturas"])
def empleados_sede_facturas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT 
            s.nombre as sede,
            COUNT(DISTINCT e.empleado_id) as total_empleados,
            COUNT(f.factura_id) as total_facturas
        FROM Sedes s
        LEFT JOIN Empleados e ON s.sede_id = e.sede_id
        LEFT JOIN Facturacion f ON e.empleado_id = f.empleado_id
        GROUP BY s.sede_id, s.nombre
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

@router.get("/query4/", tags=["query4 cliente mayor facturacion"])
def cliente_mayor_facturacion():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT 
            c.nombre,
            COUNT(f.factura_id) as total_facturas,
            SUM(f.total) as total_facturado
        FROM Clientes c
        INNER JOIN Facturacion f ON c.cliente_id = f.cliente_id
        GROUP BY c.cliente_id, c.nombre
        ORDER BY total_facturado DESC
        LIMIT 1
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()    

@router.get("/query5/", tags=["query5 productos sin proveedor"])
def productos_sin_proveedor():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT p.*
        FROM Productos p
        LEFT JOIN Proveedores pr ON p.proveedor_id = pr.proveedor_id
        WHERE p.proveedor_id IS NULL
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

@router.get("/query6/", tags=["query6 empleados top ventas"])
def empleados_top_ventas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT 
            s.nombre as sede,
            e.nombre as empleado,
            COUNT(f.factura_id) as total_ventas,
            SUM(f.total) as total_facturado
        FROM Sedes s
        INNER JOIN Empleados e ON s.sede_id = e.sede_id
        INNER JOIN Facturacion f ON e.empleado_id = f.empleado_id
        GROUP BY s.sede_id, s.nombre, e.empleado_id, e.nombre
        ORDER BY total_facturado DESC
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()  


@router.get("/query7/", tags=["query7 proveedor producto mas caro"])
def proveedor_producto_mas_caro():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT 
            p.nombre as proveedor,
            pr.nombre as producto,
            pr.precio as precio_maximo
        FROM Proveedores p
        RIGHT JOIN Productos pr ON p.proveedor_id = pr.proveedor_id
        WHERE pr.precio = (
            SELECT MAX(precio)
            FROM Productos
            WHERE proveedor_id = p.proveedor_id
        )
        ORDER BY pr.precio DESC
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


@router.get("/query8/", tags=["query8 productos stock critico"])
def productos_stock_critico():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT 
            p.*,
            pr.nombre as proveedor
        FROM Productos p
        LEFT JOIN Proveedores pr ON p.proveedor_id = pr.proveedor_id
        WHERE p.stock < 10
        ORDER BY p.stock ASC
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


@router.get("/query9/", tags=["query9 rendimiento empleados sede"])
def rendimiento_empleados_sede():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT 
            s.nombre as sede,
            e.nombre as empleado,
            COUNT(f.factura_id) as total_ventas,
            AVG(f.total) as promedio_venta
        FROM Sedes s
        INNER JOIN Empleados e ON s.sede_id = e.sede_id
        LEFT JOIN Facturacion f ON e.empleado_id = f.empleado_id
        GROUP BY s.sede_id, s.nombre, e.empleado_id, e.nombre
        ORDER BY total_ventas DESC
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


@router.get("/query10/", tags=["query10 facturacion por sede"])
def facturacion_por_sede():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT 
            s.nombre as sede,
            COUNT(f.factura_id) as total_facturas,
            SUM(f.total) as total_facturado,
            AVG(f.total) as promedio_factura
        FROM Sedes s
        INNER JOIN Empleados e ON s.sede_id = e.sede_id
        INNER JOIN Facturacion f ON e.empleado_id = f.empleado_id
        GROUP BY s.sede_id, s.nombre
        ORDER BY total_facturado DESC
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

@router.get("/query11/", tags=["query11 productos por rango de precio"])
def productos_por_rango_precio():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT 
            pr.nombre as proveedor,
            COUNT(CASE WHEN p.precio < 100 THEN 1 END) as productos_bajo_precio,
            COUNT(CASE WHEN p.precio >= 100 AND p.precio < 500 THEN 1 END) as productos_precio_medio,
            COUNT(CASE WHEN p.precio >= 500 THEN 1 END) as productos_precio_alto
        FROM Proveedores pr
        LEFT JOIN Productos p ON pr.proveedor_id = p.proveedor_id
        GROUP BY pr.proveedor_id, pr.nombre
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()        

@router.get("/query12/", tags=["query12 clientes frecuentes"])
def clientes_frecuentes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT 
            c.nombre,
            c.email,
            COUNT(f.factura_id) as total_compras,
            SUM(f.total) as total_gastado,
            AVG(f.total) as promedio_compra,
            MAX(f.fecha_factura) as ultima_compra
        FROM Clientes c
        INNER JOIN Facturacion f ON c.cliente_id = f.cliente_id
        GROUP BY c.cliente_id, c.nombre, c.email
        HAVING COUNT(f.factura_id) >= 3
        ORDER BY total_compras DESC
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


@router.get("/query13/", tags=["query13 empleados sin ventas"])
def empleados_sin_ventas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT 
            s.nombre as sede,
            e.nombre as empleado,
            COUNT(f.factura_id) as total_ventas,
            AVG(f.total) as promedio_venta
        FROM Sedes s
        INNER JOIN Empleados e ON s.sede_id = e.sede_id
        LEFT JOIN Facturacion f ON e.empleado_id = f.empleado_id
        GROUP BY s.sede_id, s.nombre, e.empleado_id, e.nombre
        ORDER BY total_ventas DESC
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


@router.get("/query14/", tags=["query14 clientes sin compras"])
def clientes_sin_compras():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT c.*
        FROM Clientes c
        LEFT JOIN Facturacion f ON c.cliente_id = f.cliente_id
        WHERE f.factura_id IS NULL
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


@router.get("/query15/", tags=["query15 top productos"])
def top_productos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT 
            p.nombre,
            p.precio,
            COUNT(f.factura_id) as veces_vendido,
            SUM(f.total) as total_generado
        FROM Productos p
        INNER JOIN Facturacion f ON p.producto_id = f.factura_id
        GROUP BY p.producto_id, p.nombre, p.precio
        ORDER BY veces_vendido DESC
        LIMIT 5
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
        


