# 🏦 Cuenta Funciones - Sistema Bancario Simple

## Descripción

**Cuenta Funciones** es un sistema de gestión bancaria básico implementado en Python mediante programación estructurada. Permite realizar operaciones fundamentales de una cuenta bancaria: depósitos, retiros y consulta de saldo.

Este proyecto forma parte de una colección educativa sobre Programación Orientada a Objetos (POO) en Python, sirviendo como punto de partida para comprender la evolución de código estructurado hacia un diseño orientado a objetos.

## ✨ Características

- **Depósito de dinero**: Agrega fondos a la cuenta con validación de cantidad positiva
- **Retiro de dinero**: Extrae fondos con validación de saldo suficiente
- **Consulta de saldo**: Muestra el saldo actual formateado a 2 decimales
- **Menú interactivo**: Interfaz de línea de comandos fácil de usar
- **Validaciones**: Control de entradas inválidas y operaciones no permitidas

## 🚀 Requisitos

- Python 3.x
- No requiere dependencias externas (usa solo la biblioteca estándar)

## 📦 Instalación

1. Clona o descarga este repositorio
2. Navega al directorio del proyecto:
   ```bash
   cd "cuenta_funciones"
   ```
3. Ejecuta el script directamente (no requiere instalación adicional)

## 🎯 Uso

Ejecuta el programa desde la terminal:

```bash
python banco.py
```

### Menú de opciones

```
Bienvenido al Banco
1. Depositar
2. Retirar
3. Mostrar saldo
4. Salir
```

### Ejemplo de sesión

```
Bienvenido al Banco
1. Depositar
2. Retirar
3. Mostrar saldo
4. Salir
Seleccione una opción: 1
Ingrese la cantidad a depositar: 500
Depósito exitoso. Su nuevo saldo es: 500.00

Seleccione una opción: 3
Su saldo actual es: 500.00

Seleccione una opción: 2
Ingrese la cantidad a retirar: 200
Retiro exitoso. Su nuevo saldo es: 300.00
```

## 📁 Estructura del Proyecto

```
cuenta_funciones/
├── banco.py          # Script principal con las funciones bancarias
└── README.md         # Documentación del proyecto
```

## 🧠 Funciones Implementadas

| Función | Descripción | Parámetros | Retorno |
|---------|-------------|------------|---------|
| `depositar()` | Agrega dinero a la cuenta | `saldo` (float) | `saldo` actualizado |
| `retirar()` | Extrae dinero de la cuenta | `saldo` (float) | `saldo` actualizado |
| `mostrar_saldo()` | Muestra el saldo actual | `saldo` (float) | None (solo imprime) |
| `main()` | Función principal con menú interactivo | None | None |

## 🔮 Próximos Pasos (POO)

Este proyecto está diseñado para ser refactorizado hacia Programación Orientada a Objetos. Las posibles mejoras incluyen:

- Crear una clase `CuentaBancaria` que encapsule el saldo y las operaciones
- Implementar clases para diferentes tipos de cuentas (Ahorro, Corriente)
- Agregar historial de transacciones
- Persistencia de datos (archivos JSON, SQLite)
- Sistema de autenticación de usuarios
- Interfaz gráfica con Tkinter o PyQt

## 📝 Notas

- El saldo inicial siempre comienza en `0.0`
- Todas las cantidades deben ser mayores a cero
- Los valores se muestran formateados a 2 decimales
- El programa se ejecuta en bucle hasta que el usuario selecciona "Salir"

## 🤝 Contribuciones

Este es un proyecto educativo. Siéntete libre de:
- Refactorizar el código usando POO
- Agregar nuevas funcionalidades
- Mejorar las validaciones
- Crear tests unitarios

## 📄 Licencia

Proyecto educativo de código abierto. Libre uso y modificación.

---

> **Nota del desarrollador:** Este proyecto demuestra los fundamentos de la programación estructurada en Python. Es un excelente punto de partida para entender cómo evolucionar hacia un diseño orientado a objetos más robusto y escalable.

---

**Creado por:** Eddy  
**Propósito:** Educativo - Aprendizaje de POO en Python
