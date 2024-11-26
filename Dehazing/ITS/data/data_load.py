import os
from PIL import Image as Image
from data import PairCompose, PairRandomCrop, PairRandomHorizontalFilp, PairToTensor
from torchvision.transforms import functional as F
from torch.utils.data import Dataset, DataLoader


def train_dataloader(path, batch_size=64, num_workers=0, data='ITS', use_transform=True):
    image_dir = os.path.join(path, 'train')

    if data == 'real_haze':
        crop_size = [800,1184]
    else:
        crop_size = 256

    transform = None
    if use_transform:
        transform = PairCompose(
            [
                PairRandomCrop(crop_size),
                PairRandomHorizontalFilp(),
                PairToTensor()
            ]
        )
    dataloader = DataLoader(
        DeblurDataset(image_dir, data, transform=transform),
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=True
    )
    return dataloader


def test_dataloader(path, data, batch_size=1, num_workers=0):
    image_dir = os.path.join(path, 'test')
    dataloader = DataLoader(
        DeblurDataset(image_dir, data, is_test=True),
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=True
    )

    return dataloader


def valid_dataloader(path, data, batch_size=1, num_workers=0):
    dataloader = DataLoader(
        DeblurDataset(os.path.join(path, 'test'), data),
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers
    )

    return dataloader


class DeblurDataset(Dataset):
    def __init__(self, image_dir, data, transform=None, is_test=False):
        self.image_dir = image_dir
        self.image_list = os.listdir(os.path.join(image_dir, 'hazy/'))
        self.image_list.sort()
        self.transform = transform
        self.is_test = is_test
        self.data = data

    def __len__(self):
        return len(self.image_list)

    def __getitem__(self, idx):
        if self.data == 'ITS':
            image = Image.open(os.path.join(self.image_dir, 'hazy', self.image_list[idx]))
            label = Image.open(os.path.join(self.image_dir, 'gt', self.image_list[idx].split('_')[0]+'.png'))
        elif self.data == 'real_haze':
            image = Image.open(os.path.join(self.image_dir, 'hazy', self.image_list[idx]))
            label = Image.open(os.path.join(self.image_dir, 'gt', self.image_list[idx]).replace('hazy', 'GT'))
        elif self.data == 'haze4k':
            image = Image.open(os.path.join(self.image_dir, 'IN', self.image_list[idx]))
            label = Image.open(os.path.join(self.image_dir, 'GT', self.image_list[idx]))

        if self.transform:
            image, label = self.transform(image, label)
        else:
            image = F.to_tensor(image)
            label = F.to_tensor(label)
        if self.is_test:
            name = self.image_list[idx]
            return image, label, name
        return image, label

