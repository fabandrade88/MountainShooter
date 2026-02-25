from game_code.Background import Background
from game_code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []

                for i in range(7):
                    bg = Background(f'Level1Bg{i}', position=(0, 0))
                    bg1 = Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0))

                    list_bg.extend([bg, bg1])   # append takes only ONE item; use extend to add both


                return list_bg

        return None