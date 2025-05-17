import pygame
from typing import Union,List,Tuple
pygame.init()

def get_color(name_of_color:Union[str,Tuple[int,int,int]]):
    """Converte o nome passado em uma tupla RGB

    Args:
        name_of_color (Union[str,Tuple[int,int,int]]): Var com o nome ou valores RGB (red, green, blue)
    Returns:
        tuple: valor (R, G, B) range(255,255,255)
    """
    COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "gray": (128, 128, 128),
    "brown": (165, 42, 42),
    "pink": (255, 192, 203),
    "lime": (0, 255, 0),
    "navy": (0, 0, 128),
    "teal": (0, 128, 128),
    "maroon": (128, 0, 0),
    "olive": (128, 128, 0),
    "gold": (255, 215, 0),
    "silver": (192, 192, 192),
    "lightgray": (211, 211, 211),
    "darkgray": (64, 64, 64),
    "skyblue": (135, 206, 235),
    "lightblue": (173, 216, 230),
    "darkblue": (0, 0, 139),
    "lightgreen": (144, 238, 144),
    "darkgreen": (0, 100, 0),
    "salmon": (250, 128, 114),
    "coral": (255, 127, 80),
    "chocolate": (210, 105, 30),
    "crimson": (220, 20, 60),
    "indigo": (75, 0, 130),
    "ivory": (255, 255, 240),
    "khaki": (240, 230, 140),
    "lavender": (230, 230, 250),
    "plum": (221, 160, 221),
    "orchid": (218, 112, 214),
    "peachpuff": (255, 218, 185),
    "peru": (205, 133, 63),
    "rosybrown": (188, 143, 143),
    "sienna": (160, 82, 45),
    "snow": (255, 250, 250),
    "tomato": (255, 99, 71),
    "turquoise": (64, 224, 208),
    "violet": (238, 130, 238),
    "wheat": (245, 222, 179),
    "mintcream": (245, 255, 250),
    "midnightblue": (25, 25, 112),
    "steelblue": (70, 130, 180),
    "slategray": (112, 128, 144),
    "lightcoral": (240, 128, 128),
    "aquamarine": (127, 255, 212),
    "aliceblue": (240, 248, 255),
    "beige": (245, 245, 220),
    "azure": (240, 255, 255),
    "blanchedalmond": (255, 235, 205),
    "blueviolet": (138, 43, 226),
    "burlywood": (222, 184, 135),
    "cadetblue": (95, 158, 160),
    "chartreuse": (127, 255, 0),
    "cornflowerblue": (100, 149, 237),
    "cornsilk": (255, 248, 220),
    "darkcyan": (0, 139, 139),
    "darkgoldenrod": (184, 134, 11),
    "darkkhaki": (189, 183, 107),
    "darkmagenta": (139, 0, 139),
    "darkolivegreen": (85, 107, 47),
    "darkorange": (255, 140, 0),
    "darkorchid": (153, 50, 204),
    "darksalmon": (233, 150, 122),
    "darkseagreen": (143, 188, 143),
    "darkslateblue": (72, 61, 139),
    "darkslategray": (47, 79, 79),
    "darkturquoise": (0, 206, 209),
    "darkviolet": (148, 0, 211),
    "deeppink": (255, 20, 147),
    "deepskyblue": (0, 191, 255),
    "dodgerblue": (30, 144, 255),
    "floralwhite": (255, 250, 240),
    "gainsboro": (220, 220, 220),
    "ghostwhite": (248, 248, 255),
    "honeydew": (240, 255, 240),
    "hotpink": (255, 105, 180),
    "indianred": (205, 92, 92),
    "lemonchiffon": (255, 250, 205),
    "linen": (250, 240, 230),
    "mistyrose": (255, 228, 225),
    "moccasin": (255, 228, 181),
    "navajowhite": (255, 222, 173),
    "oldlace": (253, 245, 230),
    "papayawhip": (255, 239, 213),
    "powderblue": (176, 224, 230),
    "seashell": (255, 245, 238),
    "seagreen": (46, 139, 87),
    "springgreen": (0, 255, 127),
    "thistle": (216, 191, 216),
    "whitesmoke": (245, 245, 245),
    "yellowgreen": (154, 205, 50)
}

    try:
        if name_of_color:
            if type(name_of_color) != tuple:
                name_of_color = name_of_color.lower()
                return COLORS[name_of_color]
            else:
                return name_of_color
    except:
        print("error, set defaut color 'black'")
        return (0,0,0)

def get_image(path_image:str):
    """Função para fazer upload de imagem

    Args:
        path_image (str): Caminho da imagem

    Returns:
        Surface: Imagem convertida pela biblioteca pygame
    """
    image = pygame.image.load(path_image)
    return image

def verify_click(rect:pygame.Rect,
                 position:Union[List[int],Tuple[int,int,int]]):
    """Verifica a região clicada

    Args:
        rect (pygame.Rect): Retangulo do pygame
        position (Union[List[int],Tuple[int,int,int]]): Lista com coordenadas, de onde foi clicado [x,y]
    Returns:
        bool: Retorna se houve colisão mause/retângulo um valor bool
    """
    clicked = rect.collidepoint(position)
    return clicked


def insert_text(text:str,
                color:Union[List[int],Tuple[int,int,int],str],
                size:int,
                background_color:str = None,
                background:str = None,
                percent_background = 10):
    """Função para inserir trasformar texto

    Args:
        text (str): Texto a ser inserido.
        color (Union[List[int],Tuple[int,int,int],str]): Cor do texto.
        size (int): tamanho do texto.
        background_color (str, opitional): Cor do fundo. Defaults to None
        background (str, optional): Caminho para imagem de fundo. Defaults to None.
        percent_background (int, optional): porcentagem de aumento da imagem. Defaults to 10.

    Returns:
        Surface: Retorna um objeto Surface
    """
    color = get_color(color)
    fonte = pygame.font.Font(None,size)
    text_render = fonte.render(text,True,color,background_color)
    returnar = text_render
    if background is not None:
        background = get_image(background)
        size_image = text_render.get_size()
        size_image = [size_image[0]+percent_background/100*size_image[0],size_image[1]+percent_background/100*size_image[1]]
        background = pygame.transform.scale(background,size_image)
        returnar = [text_render, background]
        return returnar
    

    return returnar


def get_obj_center(coordinate_size:Union[List[int],Tuple[int,int]],
                   size_objt:Union[List[int],Tuple[int,int]]):
    """Coletar um ponto central de acordo com as posições

    Args:
        coordinate_size (Union[List[int],Tuple[int,int]]): Tamanho da area na qual quer coletar o centro [x,y]
        size_objt (Union[List[int],Tuple[int,int]]): Tamanho do objeto a ser calculado [x,y]

    Returns:
        list: Retorna uma lista com os valores do centro de acordo com o tamanho do objeto
    """
    size_obj = [size_objt[0],size_objt[1]]
    center = [int(coordinate_size[0]/2 - size_obj[0]/2),int(coordinate_size[1]/2-size_obj[1]/2)]
    return center


def get_mid(object_base_coordinates:Union[List[int],Tuple[int,int]],
            object_base_size:Union[List[int],Tuple[int,int]],
            object_target_size:Union[List[int],Tuple[int,int]] = None,
            orientation:str="Todo"):
    """Função para obter as coordenadas do centro de acordo com as coordenadas informadas

    Args:
        object_base_coordinates (Union[List[int],Tuple[int,int]]): Coordenadas do objeto alvo do calculo do centro
        object_base_size (Union[List[int],Tuple[int,int]]): Tamanho do obejto alvo
        object_target_size (Union[List[int],Tuple[int,int]]): _Tamanho do objeto que estara no centro
        orientation (str): Posição que deseja encontrar. Use "Largura", "Altura", "Todo"

    Returns:
        list: Retorna as coordenadas do centro
    """
    coordinate = []
    if orientation.lower() == "largura":
        coordinate = [object_base_coordinates[0] + object_base_size[0]/2 - object_target_size[0]/2,object_base_coordinates[1]]
        
    if orientation.lower() == "altura":
        coordinate = [object_base_coordinates[0], object_base_coordinates[1] + object_base_size[1]/2 - object_target_size[1]/2]
        
    else:
        coordinate = [object_base_coordinates[0] + object_base_size[0]/2 - object_target_size[0]/2, object_base_coordinates[1] + object_base_size[1]/2 - object_target_size[1]/2]
    
    return coordinate

def furp(path:str):
    """FUCK YOU RELATIVE PATH!!!!!!!!!!!!!!!!!

    Args:
        path (str): relative path

    Returns:
        str: _relative path
    """
    return path.replace("\ ".replace(' ',''),'/')

def get_window_center(window_size: Union[List[int], Tuple[int, int]],
                        object_size: Union[List[int], Tuple[int, int]]):
    """Calcula o centro da janela com base no tamanho do objeto.

    Args:
        window_size (Union[List[int], Tuple[int, int]]): Tamanho da janela [largura, altura].
        object_size (Union[List[int], Tuple[int, int]]): Tamanho do objeto [largura, altura].

    Returns:
        list: Coordenadas do centro [x, y].
    """
    center_x = (window_size[0] - object_size[0]) // 2
    center_y = (window_size[1] - object_size[1]) // 2
    return [center_x, center_y]

def get_nested_center(window_size: Union[List[int], Tuple[int, int]],
                        object_size: Union[List[int], Tuple[int, int]],
                        nested_object_size: Union[List[int], Tuple[int, int]]):
    """Calcula o centro de um objeto aninhado dentro de outro objeto posicionado na janela.

    Args:
        window_size (Union[List[int], Tuple[int, int]]): Tamanho da janela [largura, altura].
        object_size (Union[List[int], Tuple[int, int]]): Tamanho do objeto posicionado na janela [largura, altura].
        nested_object_size (Union[List[int], Tuple[int, int]]): Tamanho do objeto aninhado [largura, altura].

    Returns:
        list: Coordenadas do centro do objeto aninhado [x, y].
    """
    object_center = get_window_center(window_size, object_size)
    nested_center_x = object_center[0] + (object_size[0] - nested_object_size[0]) // 2
    nested_center_y = object_center[1] + (object_size[1] - nested_object_size[1]) // 2
    return [nested_center_x, nested_center_y]