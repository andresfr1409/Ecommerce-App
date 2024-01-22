<h1 align="center">
  <b>FluxShopper E-commerce</b>
</h1>

![Texto Alternativo](img/FluxShopper.png)

## Nombre y descripcion 

FluxShopper es una plataforma de comercio electrónico diseñada para ofrecer a los usuarios una experiencia de compra en línea fácil y conveniente. Esta aplicación proporciona un entorno virtual donde los usuarios pueden explorar, seleccionar y comprar una amplia variedad de productos, agregandolos al carrito.

## Capturas de Pantalla

Incluye capturas de pantalla o imágenes que muestren la interfaz o funcionalidades clave de tu proyecto.

## Características 

### Exploración de Productos

Los usuarios pueden explorar una amplia gama de productos, organizados por categorías para facilitar la búsqueda.

### Carrito de Compras: 

Funcionalidad de carrito de compras que permite a los usuarios agregar, eliminar y ajustar la cantidad de productos fácilmente.

### Registro de Usuarios: 

Los usuarios pueden registrarse para crear una cuenta, lo que les permite realizar un seguimiento de sus pedidos y guardar información personal.

### Proceso de Pago por email: Integración de envio de email al usuario de los productos a comprar, al momento de gestionar el pedido del carrito de compras.

## Tecnologías Utilizadas

- Django: Marco de desarrollo web de Python para el backend.
- SQLite: Base de datos incorporada para almacenar información de los usuario, detalles de productos e informacion como entradas del blog y entradas los servicios ofrecidos.
- HTML, CSS, JavaScript: Tecnologías estándar para el desarrollo del frontend.
- Bootstrap: Utilizado para el diseño y la interfaz de usuario receptiva.

## Instalación

1. Clona el repositorio
2. Configurar el entorno virtual y instalar las dependencias con "pip install -r requirements.txt".
3. Ejecuta las migraciones con "python manage.py makemigrations" y despues ejecutar "python manage.py migrate".
4. Inicia el servidor de desarrollo local con "python manage.py runserver".

## Uso

1. Registrate o inicia sesion para poder agregar y comprar productos
2. Explora la tienda y sus diferentes secciones,  seleccionando los productos que deseas agregar al carrito.
3. Agrega productos al carrito de compras.
4. compra para que te llegue a tu email la compra realizada
