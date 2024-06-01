from src.model import *
from src.data import DataloaderHandler
import pickle
from transformers import T5EncoderModel, T5Tokenizer, logging
import os
from src.meta import BASE_DIR


class ModelAttributes:
    def __init__(self, 
                 model_type: str,
                 class_type: pl.LightningModule, 
                 alphabet, 
                 embedding_file: str, 
                 save_path: str,
                 outputs_save_path: str,
                 clip_len: int,
                 embed_len: int) -> None:
        self.model_type = model_type
        self.class_type = class_type 
        self.alphabet = alphabet
        self.embedding_file = embedding_file
        self.save_path = save_path
        if not os.path.exists(f"{self.save_path}"):
            os.makedirs(f"{self.save_path}")
        self.ss_save_path = os.path.join(self.save_path, "signaltype")
        if not os.path.exists(f"{self.ss_save_path}"):
            os.makedirs(f"{self.ss_save_path}")

        self.outputs_save_path = outputs_save_path

        if not os.path.exists(f"{outputs_save_path}"):
            os.makedirs(f"{outputs_save_path}")
        self.clip_len = clip_len
        self.embed_len = embed_len
        

def get_train_model_attributes(model_type):
    if model_type == FAST:
        with open(BASE_DIR+"models/ESM1b_alphabet.pkl", "rb") as f:
            alphabet = pickle.load(f)
        return ModelAttributes(
            model_type,
            ESM1bFrozen,
            alphabet,
            EMBEDDINGS[FAST]["embeds"],
            BASE_DIR+"models/models_esm1b",
            BASE_DIR+"outputs/esm1b/",
            1022,
            1280
        )
    elif model_type == FAST2:
        with open(BASE_DIR+"models/ESM2b_alphabet.pkl", "rb") as f:
            alphabet = pickle.load(f)
        return ModelAttributes(
            model_type,
            ESM2bFrozen,
            alphabet,
            EMBEDDINGS[FAST2]["embeds"],
            BASE_DIR+"models/models_esm2b",
            BASE_DIR+"outputs/esm2b/",
            1022,
            1280
        )
    elif model_type == MAMBA:
        # alphabet = T5Tokenizer.from_pretrained(BASE_DIR+"Rostlab/prot_t5_xl_uniref50", do_lower_case=False )
        
        # return ModelAttributes(
        #     model_type,
        #     ProtT5Frozen,
        #     alphabet,
        #     EMBEDDINGS[MAMBA]["embeds"],            
        #     BASE_DIR+"models/models_prott5",
        #     BASE_DIR+"outputs/prott5/",
        #     4000,
        #     1024
        # )
        print("MAMBA model not implemented yet")
        # TODO: Implement MAMBA model
        pass 
    elif model_type == ACCURATE:
        alphabet = T5Tokenizer.from_pretrained(BASE_DIR+"Rostlab/prot_t5_xl_uniref50", do_lower_case=False )
        
        return ModelAttributes(
            model_type,
            ProtT5Frozen,
            alphabet,
            EMBEDDINGS[ACCURATE]["embeds"],            
            BASE_DIR+"models/models_prott5",
            BASE_DIR+"outputs/prott5/",
            4000,
            1024
        )
    else:
        raise Exception("wrong model type provided expected Fast,Accurate got", model_type)
    

