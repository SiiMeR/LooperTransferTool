import click
import os

def main() -> None:
    drive = "F:"
    folder = "ROLAND/WAVE"
    path = os.path.join(drive, folder)

    slots = os.listdir(path)

    click.echo("Contents:")
    click.echo('SLOT\tFILE')
    for slotIndex in range(0, 99):
        slot = slots[slotIndex]
        file = os.listdir(os.path.join(path, slot))

        if(len(file) > 0):
            click.echo(f'Slot {slotIndex + 1}\t{file[0]}')
        else:
            click.echo(f'Slot {slotIndex + 1}\tEMPTY')


if __name__ == '__main__':
    main()
