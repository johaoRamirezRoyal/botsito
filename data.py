import pandas as pd

ARCHIVO = 'correos.csv'

df = pd.read_csv(ARCHIVO)

df_correos = df.rename(columns={
    'First Name [Required]': 'primer_nombre',
    'Last Name [Required]': 'apellido',
    'Email Address [Required]': 'email'
})

df_correos['correo_generado'] = (
    df_correos['primer_nombre']
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(' ', '', regex=False)
    + '.'
    + df_correos['apellido']
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(' ', '', regex=False)
    + '@royalschool.edu.co'
)

def devolver_correos():
    return df_correos['correo_generado'].tolist()[:500]


def eliminar_correos_enviados(correos_enviados):

    global df_correos

    # Filtrar
    df_correos = df_correos[
        ~df_correos['correo_generado'].isin(correos_enviados)
    ]

    # Guardar CSV actualizado
    df_correos.to_csv(
        ARCHIVO,
        index=False
    )

    print("✅ CSV actualizado correctamente")

    return df_correos['correo_generado'].tolist()