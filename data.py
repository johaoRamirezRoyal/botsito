import pandas as pd

df = pd.read_csv('correos.csv')

df_correos = df.rename(columns={
    'First Name [Required]': 'primer_nombre',
    'Last Name [Required]': 'apellido',
    'Email Address [Required]': 'email'
})

def devolver_correos():
    df = df_correos.copy()

    df['correo_generado'] = (
    df['primer_nombre']
    .astype(str)
    .str.strip()
    .str.lower()
    + '.' + df['apellido'] 
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(' ', '')
    + '@royalschool.edu.co'
    )

    correos = df['correo_generado'].tolist()
    return correos[:500]

def eliminar_correos_enviados(correos_enviados):
    df = df_correos.copy()

    df['correo_generado'] = (
    df['primer_nombre']
    .astype(str)
    .str.strip()
    .str.lower()
    + '.' + df['apellido'] 
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(' ', '')
    + '@royalschool.edu.co'
    )

    df_filtrado = df[~df['correo_generado'].isin(correos_enviados)]

    correos_restantes = df_filtrado['correo_generado'].tolist()
    
    return correos_restantes