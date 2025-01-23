from src import AVL_tree, Comment
from random import randint

def main():
    print("\n---------------------TASK 1-3 ---------------------\n")
    tree = AVL_tree()

    for i in range(0,15):
        val=randint(1,101)
        tree.insert_value(val)


    tree.print2DTree()
    print(f"Max values: {tree.max_value_node()}\n")
    print(f"Min values: {tree.min_value_node()}\n")
    print(f"Sum values: {tree.sum_values()}")

    print("\n---------------------TASK 4---------------------\n")

    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    # reply1.remove_reply()

    root_comment.display()



# if __name__ == "__main___":
#     try: 
#         main()
#     except Exception as e:
#         print(e)
    
main()