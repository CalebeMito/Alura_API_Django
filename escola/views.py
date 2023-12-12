from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        # Retorna todos os dados dos alunos cadastrados no banco de dados
        aluno = {'id': 1, 'nome':'Guilherme' }
        return JsonResponse(aluno)


