from bs4 import BeautifulSoup

a = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
        <SalvaSinistroWS xmlns="http://tempuri.org/">
            <identificacao>
                <Corretora>SEGURALTA</Corretora>
                <Usuario>grupowdg</Usuario>
                <Senha>wdg@042018</Senha>
            </identificacao>
            <objSinistroWS>
                <Proprietario>DRESSFIRE INSTALACOES INDUSTRIAIS E LOCACOES</Proprietario>
                <Documento>1664766</Documento>
                <Apolice>5177202126312397899</Apolice>
                <CpfCnpjCliente>26132674000133</CpfCnpjCliente>
                <SinistroCia>000000</SinistroCia>
                <Reclamante>Ambos</Reclamante>
                <TipoControle>Veiculos</TipoControle>
                <DataSinistro>2022-08-30T00:00:00</DataSinistro>
                <DataAviso>2022-08-31T00:00:00</DataAviso>
                <PerdaTotal>IndenizacaoTotalSEMCancelamentoApolice</PerdaTotal>
                <Beneficiario>DRESSFIRE INSTALACOES INDUSTRIAIS E LOCACOES</Beneficiario>            
                <NomeFabricante>FIAT</NomeFabricante>
                <Modelo xsi:nil="true" />
                <DescrModelo>DOBLO ADVENTURE LOCKER 1.8 16V FLEX</DescrModelo>
                <Placa>FBM0864</Placa>
                <Chassi>9BD119409C1088562</Chassi>
                <AnoModelo>2000</AnoModelo>
                <Motorista>ARTHUR GABRIEL</Motorista>
                <CartHabilitacao>00000000000</CartHabilitacao>
                <DataAcidente>2022-08-30T00:00:00</DataAcidente>
                <LocalAcidente>RUA ADIMAR XAVIER MACHADO</LocalAcidente>
                <BairroAcidente>VILA TONINHO</BairroAcidente>
                <CidadeAcidente>SAO JOSE DO RIO PRETO</CidadeAcidente>
                <EstadoAcidente>SP</EstadoAcidente>
                <UsouGuincho>false</UsouGuincho>            
                <TemBoletim>NaoInformado</TemBoletim>
                <AssumiuCulpa>true</AssumiuCulpa>
                <DescricaoOcorrencia>Tipo: Colisão
        Colisão: Perda Total
        CEP do Acidente: 15077190
        Culpa: Segurado
    
        TESTE DE DEV NAO AVISAR POR FAVOR</DescricaoOcorrencia>            
                <NumCnh>00000000000</NumCnh>
                <CategCnh></CategCnh>            
                <Revisado>false</Revisado>
                <ItemCia xsi:nil="true" />
            </objSinistroWS>
            </SalvaSinistroWS>
        </soap:Body>
    </soap:Envelope>"""

b = BeautifulSoup(a, features="xml")

print(b.SalvaSinistroWS.objSinistroWS.DescrModelo.text)