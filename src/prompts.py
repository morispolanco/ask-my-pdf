# INFO: some prompts are still in model.py

# TODO: Ignore OCR problems in the text below.

TASK = {   
    'Pregunta + cita': (
        "Responda a la pregunta con la verdad basándote en el texto de abajo. "
        "Incluya la cita textual y un comentario de dónde encontrarla en el texto (número de página). "
        "Después de la cita, escriba una explicación paso a paso. "
        "Utilice viñetas."
    ),
    'Caso': (
        "Resuelva el caso que se te plantea basándose en el texto que aparece a continuación. "
        "Incluya al menos una cita textual (marcada con comillas) y un comentario sobre dónde encontrarla en el texto (es decir, número de artículo y número de página). "
    ),
    'Citas': (
        "A la pregunta '¿cuáles son las citas más importantes?', responda eligiendo entr tres y doce citas del artículo o libro de abajo. " 
        
    ),
    'Puntos clave': (
        "Lea detenidamente contratos y documentos legales e informa después a sus clientes sobre los puntos clave de esos documentos. "
	"Su respuesta debe ser clara y concisa, explicando con precisión los términos y condiciones del contrato o documento en cuestión. "
	"Tendrá que identificar cualquier aspecto que pueda suponer un riesgo para el cliente y ofrecerle recomendaciones específicas para solucionar esos problemas. "
	"Además, tendrá que asegurarse de que el lenguaje utilizado es accesible para su cliente, evitando tecnicismos innecesarios y proporcionando definiciones claras cuando sea necesario. " 
    ),
    'Resumen': (
        "Resuma el texto de abajo."
	"Use viñetas. "
     ),
    'Libre': (
        "Haga lo que se le pide en relación al texto que se le proporciona."
    ),
}

HYDE = "Escriba una respuesta de ejemplo a la siguiente pregunta. No escriba una respuesta genérica, asuma todo lo que no se sabe."

SUMMARY = {
    'v2': 'Describa el documento del que se extrae el fragmento. Omita cualquier detalle.',
    'v1': 'Describe el documento del que se extrae el fragmento. No describa el fragmento, céntrese en averiguar de qué tipo de documento se trata.',
}
