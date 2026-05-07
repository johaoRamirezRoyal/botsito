import pandas as pd

df = pd.read_csv('correos.csv')

df_correos = df.rename(columns={
    'First Name [Required]': 'primer_nombre',
    'Last Name [Required]': 'apellido',
    'Email Address [Required]': 'email'
})

def devolver_correos(df):
    df = df.copy()

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
