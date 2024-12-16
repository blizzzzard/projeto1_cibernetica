# projeto1_cibernetica

Projeto 1 - Disciplina: PPMEC0070 - CIBERNÉTICA E APRENDIZAGEM DE MÁQUINA 
Nome: Andrey Otacílio Oliveira dos Reis  Matrícula: 241131482


Inicialmente o dataset deve ser preparado:

```shell
python data_conversion.py
```

Treinamento:
```shell
python tools/train.py -c configs/rtdetr/rtdetr_r101vd_6x_coco.yml
```

Teste:
```shell
python tools/train.py -c configs/rtdetr/rtdetr_r101vd_6x_coco.yml -r checkpoint --test-only
```

Inferência:
```shell
python tools/infer.py -c configs/rtdetr/rtdetr_r101vd_6x_coco.yml -r checkpoint -f file_image
```
