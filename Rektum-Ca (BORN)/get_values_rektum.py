def get_analkanal(root):
    analkanal_neg = root.xpath('//Question[@Question="Analkanal Beteiligung"]/Options/Value[@Answer="Anal -"]/@Selected')
    analkanal_pos = root.xpath('//Question[@Question="Analkanal Beteiligung"]/Options/Value[@Answer="Anal +"]/@Selected')

    if analkanal_neg[0] == "true" and analkanal_pos[0] == "false":
        return False
    
    if analkanal_neg[0] == "false" and analkanal_pos[0] == "true":
        return True
    else:
        return None
    
def get_MRF(root):
    MRF_neg = root.xpath('//Question[@Question="MRF Status"]/Options/Value[@Answer="MRF -"]/@Selected')
    MRF_pos = root.xpath('//Question[@Question="MRF Status"]/Options/Value[@Answer="MRF +"]/@Selected')

    if MRF_neg[0] == "true" and MRF_pos[0] == "false":
        return False
    
    if MRF_neg[0] == "false" and MRF_pos[0] == "true":
        return True
    else:
        return None
    
def get_EMVI(root):
    EMVI_neg = root.xpath('//Question[@Question="EMVI Status"]/Options/Value[@Answer="EMVI -"]/@Selected')
    EMVI_pos = root.xpath('//Question[@Question="EMVI Status"]/Options/Value[@Answer="EMVI +"]/@Selected')

    if EMVI_neg[0] == "true" and EMVI_pos[0] == "false":
        return False
    
    if EMVI_neg[0] == "false" and EMVI_pos[0] == "true":
        return True
    else:
        return None
    
def get_höhe_tumor_oberrand(root):
    
    höhe = root.xpath('//Question[@Label="Höhe des Tumor-Oberrandes ab ano"]/@Answer')

    for h in höhe:
        if len(h)>0:
            return (float(h), "mm")

    return None

def get_höhe_tumor_unterrand(root):
    
    sop_instance = root.xpath('//GenericMeasurement[@Label="Höhe des Tumor-Unterrandes ab ano"]/MeasurementRecord/@SOPInstanceUID')

    höhe = root.xpath('//GenericMeasurement[@Label="Höhe des Tumor-Unterrandes ab ano"]/MeasurementRecord/MeasurementQuantity[@Type="distance"]/@DisplayedValue')

    for h in höhe:
        if len(h)>0:
            return (float(h), "mm", sop_instance[0])

    return None

def get_TNM(root):
    
    T = root.xpath('//Question[@Label="T-Kategorie"]/@Answer')

    N = root.xpath('//Question[@Label="N-Kategorie"]/@Answer')

    M = root.xpath('//Question[@Label="M-Kategorie"]/@Answer')

    if T == [''] and N == [''] and M == ['']:
        return None
    
    if N == [''] and M == ['']:
        return ([str(T[0])])

    if M == ['']:
        return (str(T[0]),str(N[0]))
    
    return (str(T[0]),str(N[0]),str(M[0]))