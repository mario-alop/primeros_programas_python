# Nota de examen.

print('Programa que calcula el aprobado en un examen.')

nota = int(input('Introduzca la nota del examen: '))

aprobado = 5
notable = 7
sobresaliente = 9
m_honor = 10

if nota < aprobado:
    print('Suspenso.')
elif nota >= aprobado and nota < notable:
    print('Aprobado.')
elif nota >= notable and nota < sobresaliente:
    print('Notable.')
elif nota >= sobresaliente and nota < m_honor:
    print('Sobresaliente.')
elif nota == m_honor:
    print('Matricula de Honor, muy bien')
else:
    print('No has introducido una nota valida.')

