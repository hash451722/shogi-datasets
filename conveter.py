import pathlib

import numpy as np
from PIL import Image



def disp(img_array:np.ndarray):
    img = Image.fromarray(img_array)
    img.show()


def list_imgs_path(path_dir:pathlib.Path) -> list[pathlib.Path]:
    img_path_list = list(path_dir.glob('**/*.png')) + list(path_dir.glob('**/*.jpg'))
    return img_path_list


def img2dict(img_path_list:list[pathlib.Path]) -> dict:
    d = {"em":[], "fu":[], "gi":[], "hi":[], "ka":[], "ke":[], "ki":[], "ky":[],
         "ng":[], "nk":[], "ny":[], "ou":[], "ry":[], "to":[], "um":[]}

    for p in img_path_list:
        label = p.parent.name  # Directory name
        img_pil = Image.open(p)
        img_ndarray = np.array(img_pil, dtype=np.uint8)

        if label in d:
            d[label].append(img_ndarray)
        else:
            print("ERROR")
            d[label] = [img_ndarray]
    return d


def savez(d:dict, path_save:pathlib.Path) -> None:
    np.savez_compressed("piece", 
        em=d["em"], fu=d["fu"], gi=d["gi"], hi=d["hi"], ka=d["ka"], ke=d["ke"], ki=d["ki"], ky=d["ky"],
        ng=d["ng"], nk=d["nk"], ny=d["ny"], ou=d["ou"], ry=d["ry"], to=d["to"], um=d["um"]
        )


def load(path_npz:pathlib.Path):
    pieces_np = np.load(path_npz)
    for k, v in pieces_np.items():
        print(k, v.shape, type(v))




if __name__ == '__main__':
    path_current_dir = pathlib.Path(__file__).parent
    # path_img_dir = path_current_dir.parent.joinpath("piece_images", "test")
    path_img_dir = path_current_dir.parent.joinpath("piece_images", "train_validate")

    # Save
    path_imgs = list_imgs_path(path_img_dir)
    d = img2dict(path_imgs)
    savez(d)

    # Load
    load(path_current_dir.joinpath("piece.npz"))
