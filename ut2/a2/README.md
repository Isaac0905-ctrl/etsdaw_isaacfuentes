#  Comparación de Modelos de Desarrollo de Software y Gestión de Fallos

##  Tabla Comparativa de Modelos de Desarrollo:



| Característica / Aspecto | Modelos Clásicos (Predictivos) | Modelos Evolutivos o Incrementales | Metodologías Ágiles (Adaptativas) |
|--------------------------|---------------------------------|-------------------------------------|------------------------------------|
| **Definición Principal** | Se trabaja siguiendo un plan fijo y ordenado. Todo se define antes de empezar y se avanza fase por fase. | El software se construye por partes (versiones). Cada una mejora o amplía la anterior. | Se trabaja en ciclos pequeños donde se escucha al cliente y se aceptan cambios durante el proyecto. |
| **Características Clave / Enfoque** | Secuencia rígida: análisis → diseño → implementación → pruebas. Cambiar algo es difícil. | Entregas parciales y funcionales. Permite mejorar poco a poco. | Trabajo en equipo, comunicación constante y cambios frecuentes. |
| **Ventajas (Pros)** | Muy estructurado y fácil de seguir. Útil si los requisitos no cambian. | Permite ver resultados pronto. Fácil mejorar en la siguiente versión. | Muy flexible. Se adapta rápido a los cambios del cliente. |
| **Desventajas (Contras)** | Poco flexible. Modificar algo tarde es costoso. | Puede ser difícil saber cuántas versiones serán necesarias. | Requiere mucha participación del cliente. Puede sentirse menos "formal". |
| **Aportación en la Actualidad** | Se usa en proyectos muy estables o críticos donde todo debe estar perfectamente definido. | Es común en proyectos por módulos donde se avanza paso a paso. | Es el enfoque más utilizado hoy por su rapidez y adaptabilidad. |

---

##  Reflexión sobre la Detección y Corrección de Fallos y Cambios

### Corrección de cambios y fallos en diferentes modelos

###  Modelo en Cascada con Realimentación
En el modelo en cascada con realimentación se permite volver a una fase anterior cuando aparece un error. Aunque esto ayuda a corregir fallos, sigue siendo un proceso lento, ya que el modelo fue pensado para seguir un orden fijo. Volver atrás implica revisar decisiones tomadas desde el inicio, por lo que los cambios son costosos y se intenta evitarlos.

###  Modelos Evolutivos o Incrementales
En los modelos evolutivos o incrementales el sistema se construye por versiones. Esto facilita mucho la corrección, porque cada versión permite mejorar lo que ya existe. Los usuarios pueden probar el software antes de que esté completo, lo que genera comentarios rápidos que ayudan a detectar fallos y a cambiarlos sin rehacerlo todo. La realimentación es constante y el sistema se va refinando en cada incremento.

###  Metodologías Ágiles (Scrum, XP, etc.)
Las metodologías ágiles aceptan que cambiar es normal. Gracias a las iteraciones cortas (sprints), los errores se descubren pronto y se corrigen dentro de la misma iteración o en la siguiente. La comunicación con el cliente es continua y esto hace que cualquier cambio pueda incorporarse sin que afecte demasiado al resto del proyecto. En XP las mejoras pequeñas y constantes ayudan a que el código siempre esté listo para cambiar cuando sea necesario.

---

## Papel de la Fase de Mantenimiento

La fase de mantenimiento es una parte esencial del ciclo de vida del software, porque empieza cuando el sistema ya está en uso real. Aquí se corrigen fallos que no se detectaron antes y se adapta el software a nuevas necesidades con el paso del tiempo.

- **Mantenimiento correctivo:** se encarga de arreglar errores que aparecen cuando los usuarios empiezan a usar el sistema.
- **Mantenimiento evolutivo:** añade funciones nuevas que los usuarios necesitan para mejorar el sistema.
- **Mantenimiento adaptativo:** se ocupa de actualizar el software cuando el entorno cambia, como nuevos sistemas operativos o nuevos dispositivos.



