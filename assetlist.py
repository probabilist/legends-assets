"""Generates a list of text assets in Star Trek: Legends.

When run from the command list, calls the `assetList` function. See its
docstring for more details.

"""

from os import getcwd
import UnityPy

def assetList():
    """writes an alphabetized list of Star Trek: Legends text assets to
    a file named 'assetList.txt' in the current working directory. The
    text is formatted in a way so that it can be directly copied into
    'LegendsData/Program.cs' inside the Asset Studios C# solution.

    """
    bindataPath = (
        '/Applications/Star Trek.app/Contents/'
        + 'Resources/Data/StreamingAssets/AssetBundles/OSX/OSXRed/bindata'
    )
    env = UnityPy.load(bindataPath)
    aList = []
    for obj in env.objects:
        if not obj.type == 'TextAsset':
            continue
        data = obj.read()
        aList.append('convertBytesToJson("' + data.name + '");')
    aList.sort()
    with open(getcwd() + '/assetlist.txt', 'w', encoding='utf-8') as f:
        for line in aList:
            f.write(line + '\n')

if __name__ == '__main__':
    assetList()
