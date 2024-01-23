<h1 align="center">
  <b>FluxShopper E-commerce</b>
</h1>

<p align="center">
  <img src="Ecommerce/static/Ecommerce/img/FluxShopper.png" alt="FluxShopper">
</p>

## Nombre y descripcion 

FluxShopper es una plataforma de comercio electrónico diseñada para ofrecer a los usuarios una experiencia de compra en línea fácil y conveniente. Esta aplicación proporciona un entorno virtual donde los usuarios pueden explorar, seleccionar y comprar una amplia variedad de productos, agregandolos al carrito.

## Capturas de Pantalla

pendiente

## Características 

- ### Exploración de Productos

Los usuarios pueden explorar una amplia gama de productos, organizados por categorías para facilitar la búsqueda.

- ### Carrito de Compras

Funcionalidad de carrito de compras que permite a los usuarios agregar, eliminar y ajustar la cantidad de productos fácilmente.

- ### Registro de Usuarios

Los usuarios pueden registrarse para crear una cuenta, lo que les permite realizar un seguimiento de sus pedidos y guardar información personal.

- ### Proceso de Pago por email

Integración de envio de email al usuario de los productos a comprar, al momento de gestionar el pedido del carrito de compras.

## Tecnologías Utilizadas

- ### Django 

En FluxShopper, Django se utiliza como el motor principal del backend. Proporciona una arquitectura MVT sólida, facilitando la organización y la implementación eficiente de lógica de negocios. Django también incluye características incorporadas como la administración de bases de datos, autenticación de usuarios y generación de formularios que aceleran el desarrollo.

- ### SQLite

En FluxShopper, SQLite cumple el papel de la base de datos, almacenando información vital como detalles de productos, usuarios y transacciones. Aunque es ideal para proyectos más pequeños, Django permite la fácil migración a sistemas de gestión de bases de datos más robustos a medida que el proyecto escala.

- ### HTML, CSS, JavaScript

Estas tecnologías web fundamentales se utilizan para construir el frontend de FluxShopper. HTML define la estructura de las páginas web, CSS maneja la presentación y el diseño, y JavaScript se encarga de la interactividad del usuario. La combinación de estas tecnologías proporciona una interfaz de usuario dinámica y receptiva.

- ### Bootstrap

FluxShopper aprovecha Bootstrap para garantizar que la aplicación sea visualmente atractiva en una variedad de dispositivos y tamaños de pantalla. Además, los componentes predefinidos de Bootstrap agilizan el desarrollo al proporcionar elementos listos para usar, como barras de navegación, botones y formularios.

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
