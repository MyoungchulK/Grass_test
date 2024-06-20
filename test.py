import click
import numpy as np

@click.command()
@click.option('-i1', '--input1', default = '5', type = str)
@click.option('-i2', '--input2', default = '1 2 3 4 5', type = str)
def main(input1, input2):

    num_gras = int(input1)
    gra_val = np.asarray(input2.split(' '), dtype = int)
    print(num_gras, gra_val)

    gra_sort = np.sort(gra_val)
    max_1st = gra_sort[-1]
    gra_max = np.full((num_gras), max_1st, dtype = int)
    gra_max[gra_val == max_1st] = gra_sort[-2]
    print(gra_max)
     
if __name__ == "__main__":
    main()
