#### PLEASE, ALL THE HANDOVERS YOU NEED FOR BEACON TO SHOW LIKE THE handover_1 EXAMPLE BELOW #####

handover_1={
    "note": "Please send any data access enquiries to cardinal@populationgenomics.org.au",
    "url": "mailto:cardinal@populationgenomics.org.au",
    "handoverType": {
                    'id': 'CUSTOM',
                    'label': 'Please email to discuss data access formats'
                }
}

#### PLEASE, ADD THE HANDOVER VARIABLES FROM ABOVE YOU WANT TO ADD TO BEACON TO THE list_of_handovers VARIABLE BELOW #####
list_of_handovers=[handover_1]


#### PLEASE, ALL THE HANDOVERS PER DATASET YOU NEED FOR BEACON TO SHOW LIKE THE dataset1_handover EXAMPLE BELOW #####


dataset1_id='test' # This has to match the id for the dataset

dataset1_handover={"dataset": dataset1_id, "handover": handover_1}


#### PLEASE, ADD THE HANDOVER PER DATASET VARIABLES FROM ABOVE YOU WANT TO ADD TO BEACON TO THE list_of_handovers_per_dataset VARIABLE BELOW #####

list_of_handovers_per_dataset=[dataset1_handover]
