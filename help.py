import json
import re
import random
from pages.models import (
    Pessoa,
    Name,
    Location,
    Coordinate,
    Timezone,    
    Picture,
    Phone,
    Cell
)


def seed_db():

    """
        Importando os dados para o banco de dados
    """
    data = None

    with open('people.json', 'r') as f:
            data = json.loads(f.read())
    
    for pessoa in data['results']:
       
        # format gender
        if pessoa['gender'] == 'male':
            pessoa['gender'] = 'M'
        else:
            pessoa['gender'] = 'F'

        pattern_space = re.compile(r"[-| |\)]")
        pattern_ddi = re.compile(r"\(")
        
        # format phone
        pessoa['phone'] = pattern_space.sub("", pessoa['phone'])
        pessoa['phone'] = pattern_ddi.sub("+55", pessoa['phone'])

        # format cell
        pessoa['cell'] = pattern_space.sub("", pessoa['cell'])
        pessoa['cell'] = pattern_ddi.sub("+55", pessoa['cell'])

        # definindo a regiao
        regiao = ''
        if pessoa['location']['state'] in ('goiás', 'mato grosso', 'mato grosso do sul', 'distrito federal'):
            regiao = 'Centro-oeste'
        elif pessoa['location']['state'] in ('alagoas', 'bahia', 'ceará', 'maranhão', 'paraíba',\
                                                'pernambuco', 'piauí', 'rio grande do norte', 'sergipe'):
            regiao = 'Nordeste'
        elif pessoa['location']['state'] in ('acre', 'amapá', 'amazonas', 'pará', 'rondônia', 'roraima', 'tocantins'):
            regiao = 'Norte'
        elif pessoa['location']['state'] in ('espírito santo', 'minas gerais', 'rio de janeiro', 'são paulo'):
            regiao = 'Sudeste'
        else:
            regiao = 'Sul'

        if Pessoa.objects.filter(
            gender=pessoa['gender'],
            email=pessoa['email'],
            birthday=pessoa['dob']['date'],
            registered=pessoa['registered']['date']
        ).exists():
            
            continue
    
        Pessoa(
            gender=f"{pessoa['gender']}", 
            email=f"{pessoa['email']}",
            birthday=f"{pessoa['dob']['date']}", 
            registered=f"{pessoa['registered']['date']}",
            regiao=regiao
        ).save()
        
        p = Pessoa.objects.order_by().last()
        
        Name(
            title=f"{pessoa['name']['title']}", 
            first=f"{pessoa['name']['first']}", 
            last=f"{pessoa['name']['last']}", 
            pessoa=p
        ).save()

        Location(
            street=f"{pessoa['location']['street']}",
            city=f"{pessoa['location']['city']}",
            state=f"{pessoa['location']['state']}",
            postcode=f"{pessoa['location']['postcode']}",            
            pessoa=p
        ).save()
        l=Location.objects.order_by().last()
        Coordinate(
            latitude=f"{pessoa['location']['coordinates']['latitude']}",
            longitude=f"{pessoa['location']['coordinates']['longitude']}",
            location=l
        ).save()

        timezone=Timezone(
            offset=f"{pessoa['location']['timezone']['offset']}",
            description=f"{pessoa['location']['timezone']['description']}",
            location=l
        ).save()

        picture = Picture(
            large=f"{pessoa['picture']['large']}",
            medium=f"{pessoa['picture']['medium']}",
            thumbnail=f"{pessoa['picture']['thumbnail']}",
            pessoa=p
        ).save()

        Phone(
            phone=f"{pessoa['phone']}",
            pessoa=p
        ).save()

        Cell(
            cell=f"{pessoa['cell']}",
            pessoa=p
        ).save()

        

        