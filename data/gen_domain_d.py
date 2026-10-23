#!/usr/bin/env python3
"""Generate Domain D (Data Handling) 80 Exam-Grade MCQs for PTCA Prep."""

import json
from pathlib import Path

D1 = "D1: Dataset Fundamentals (Map-Style vs Iterable-Style & Custom Datasets)"
D2 = "D2: DataLoader Configuration, Batching, Sampling & Performance"
D3 = "D3: Transforms, Preprocessing, Data Splits, Data Leakage & Reproducibility"

QUESTIONS = [
    # =========================================================================
    # D1: Dataset Fundamentals (PTCA-D-001 to PTCA-D-022, 22 questions)
    # =========================================================================
    {
        "id": "PTCA-D-001",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "In PyTorch's `torch.utils.data` architecture, why are data primitives (`Dataset` and `DataLoader`) "
            "explicitly separated from the `nn.Module` model definition and training loop?"
        ),
        "code": "",
        "options": {
            "A": "Because `nn.Module` cannot accept raw tensors directly and requires a `DataLoader` wrapper to invoke `.forward()`.",
            "B": "To decouple data storage, preprocessing, and minibatch iteration from model training logic for better readability, modularity, and maintainability.",
            "C": "Because PyTorch's autograd engine only tracks gradients on tensors yielded by a `torch.utils.data.Dataset` subclass.",
            "D": "To force all datasets to be loaded entirely into GPU VRAM prior to initializing model weights."
        },
        "correct": ["B"],
        "explanation": (
            "As highlighted in Module 4 (`pytorch_data_utilities.ipynb`), code for processing data samples can get messy "
            "and hard to maintain; PyTorch provides `Dataset` (which stores/retrieves individual samples and labels) and "
            "`DataLoader` (which wraps an iterable around the `Dataset` for batching, shuffling, and multiprocessing) to "
            "decouple dataset code from model training code."
        ),
        "option_explanations": {
            "A": "Incorrect. `nn.Module` accepts any appropriately shaped `torch.Tensor` directly regardless of whether it came from a `DataLoader`.",
            "B": "Correct. Decoupling data handling from training code improves modularity, readability, and reusability across experiments.",
            "C": "Incorrect. Autograd tracks operations on any tensor with `requires_grad=True`, independent of `Dataset`.",
            "D": "Incorrect. `Dataset` typically loads samples lazily on the CPU rather than preloading the entire dataset into GPU memory."
        },
        "competency": "Explain the architectural role of Dataset and DataLoader in decoupling data pipelines from model code",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb"
    },
    {
        "id": "PTCA-D-002",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "You are loading the `FashionMNIST` dataset from `torchvision.datasets` as shown below. "
            "What are the respective sample counts in `training_data` and `test_data`, and what does `training_data[0]` return?"
        ),
        "code": (
            "from torchvision import datasets\n"
            "from torchvision.transforms import ToTensor\n\n"
            "training_data = datasets.FashionMNIST(\n"
            "    root='data', train=True, download=True, transform=ToTensor()\n"
            ")\n"
            "test_data = datasets.FashionMNIST(\n"
            "    root='data', train=False, download=True, transform=ToTensor()\n"
            ")"
        ),
        "options": {
            "A": "50,000 training and 10,000 test examples; `training_data[0]` returns a dictionary `{'image': tensor, 'label': int}`.",
            "B": "60,000 training and 10,000 test examples; `training_data[0]` returns a tuple `(image_tensor, label_int)` where `image_tensor` has shape `(1, 28, 28)`.",
            "C": "60,000 training and 10,000 test examples; `training_data[0]` returns a 4D batch tensor of shape `(1, 1, 28, 28)`.",
            "D": "70,000 training and 10,000 test examples; `training_data[0]` returns a PIL Image and a one-hot encoded label tensor."
        },
        "correct": ["B"],
        "explanation": (
            "`FashionMNIST` contains 60,000 training examples (`train=True`) and 10,000 test examples (`train=False`). "
            "Indexing `training_data[0]` invokes `__getitem__(0)` and returns a `(feature, label)` tuple: a float32 tensor "
            "of shape `(1, 28, 28)` (converted by `ToTensor()`) and an integer class index in `0..9`."
        ),
        "option_explanations": {
            "A": "Incorrect. `FashionMNIST` has 60,000 training samples (CIFAR-10 has 50,000), and indexing returns a 2-tuple, not a dict.",
            "B": "Correct. `FashionMNIST` has 60,000 train and 10,000 test samples, and indexing yields `(Tensor[1, 28, 28], int)`.",
            "C": "Incorrect. A `Dataset` returns a single unbatched 3D image tensor `(1, 28, 28)` together with its label, not a 4D tensor.",
            "D": "Incorrect. Because `transform=ToTensor()` is passed, the image is converted from a PIL Image to a Tensor, and labels are integer indices unless `target_transform` is specified."
        },
        "competency": "Configure pre-loaded torchvision datasets and inspect returned sample structures",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb"
    },
    {
        "id": "PTCA-D-003",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Easy",
        "multi_select": True,
        "stem": (
            "Which TWO special (dunder) methods MUST a custom map-style dataset implement when subclassing "
            "`torch.utils.data.Dataset` so that it works with `len(dataset)` and `DataLoader` default index sampling?"
        ),
        "code": (
            "from torch.utils.data import Dataset\n\n"
            "class CustomTabularDataset(Dataset):\n"
            "    def __init__(self, features, labels):\n"
            "        self.features = features\n"
            "        self.labels = labels\n"
            "    # Which two methods are required here?"
        ),
        "options": {
            "A": "`__getitem__(self, idx)`",
            "B": "`__iter__(self)`",
            "C": "`__len__(self)`",
            "D": "`__next__(self)`"
        },
        "correct": ["A", "C"],
        "explanation": (
            "A map-style dataset in PyTorch implements the `Dataset` protocol by defining `__getitem__(self, idx)` to "
            "fetch a sample given an index/key and `__len__(self)` to return the total number of samples (required by "
            "`SequentialSampler` and `RandomSampler` in `DataLoader`)."
        ),
        "option_explanations": {
            "A": "Correct. `__getitem__(self, idx)` maps an integer index to the corresponding data sample.",
            "B": "Incorrect. `__iter__(self)` is required for `IterableDataset`, not map-style `Dataset`.",
            "C": "Correct. `__len__(self)` returns the size of the dataset so samplers know the valid index range.",
            "D": "Incorrect. `__next__(self)` is part of a Python iterator, not the map-style `Dataset` interface."
        },
        "competency": "Implement custom map-style Dataset classes with __len__ and __getitem__",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb & LFD2001 Ch. 2"
    },
    {
        "id": "PTCA-D-004",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "A developer writes the custom `Dataset` class below and passes it to `DataLoader(ds, batch_size=16, shuffle=True)`. "
            "What happens when the training loop executes `for x, y in loader:`?"
        ),
        "code": (
            "import torch\n"
            "from torch.utils.data import Dataset, DataLoader\n\n"
            "class SensorRows(Dataset):\n"
            "    def __init__(self):\n"
            "        self.x = torch.randn(100, 8)\n"
            "        self.y = torch.randint(0, 2, (100,))\n\n"
            "    def __getitem__(self, idx):\n"
            "        return self.x[idx], self.y[idx]\n\n"
            "ds = SensorRows()\n"
            "loader = DataLoader(ds, batch_size=16, shuffle=True)"
        ),
        "options": {
            "A": "The `DataLoader` automatically infers the length as 100 by inspecting `self.x.shape[0]`.",
            "B": "A `TypeError: object of type 'SensorRows' has no len()` is raised when `DataLoader` initializes `RandomSampler(ds)`.",
            "C": "The loop runs infinitely because `__getitem__` wraps around negative indices.",
            "D": "It iterates until `self.x[idx]` raises an `IndexError` at `idx=100` and cleanly stops."
        },
        "correct": ["B"],
        "explanation": (
            "When `shuffle=True`, `DataLoader` constructs a `RandomSampler(dataset)` during `__init__`, which immediately "
            "checks `len(data_source)`. Because `SensorRows` omitted `__len__(self)`, calling `len(ds)` raises "
            "`TypeError: object of type 'SensorRows' has no len()`."
        ),
        "option_explanations": {
            "A": "Incorrect. `Dataset` does not introspect instance attributes like `self.x` to guess the dataset length.",
            "B": "Correct. Omitting `__len__` causes `len(ds)` to fail with `TypeError` when `DataLoader` sets up its sampler.",
            "C": "Incorrect. `DataLoader` does not iterate without a sampler, and its default samplers require `len(dataset)`.",
            "D": "Incorrect. While old Python `for item in ds:` fallback iteration relies on `IndexError`, `DataLoader` uses a `Sampler` that calls `len(ds)` upfront."
        },
        "competency": "Diagnose missing __len__ errors in custom map-style Datasets",
        "source": "LFD2001 Ch. 2"
    },
    {
        "id": "PTCA-D-005",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "When should you subclass `torch.utils.data.IterableDataset` instead of a map-style `torch.utils.data.Dataset`?"
        ),
        "code": "",
        "options": {
            "A": "Whenever the dataset contains images that need `torchvision.transforms` applied on the fly.",
            "B": "When data arrives from a continuous live stream, a remote message queue, or massive log files where random index access `dataset[idx]` is prohibitively expensive or impossible.",
            "C": "Whenever you want `DataLoader` to automatically shuffle the entire dataset across epochs using `shuffle=True`.",
            "D": "When the dataset fits entirely in CPU RAM as NumPy arrays and you want the fastest random minibatch sampling."
        },
        "correct": ["B"],
        "explanation": (
            "As explained in `pytorch_data_utilities.ipynb`, an `IterableDataset` represents an iterable stream of data "
            "samples by implementing `__iter__()`. It is suited for streaming data, very large datasets where random reads "
            "are costly, or data generated dynamically on the fly (e.g., logs or sensor feeds)."
        ),
        "option_explanations": {
            "A": "Incorrect. Map-style datasets apply `torchvision.transforms` on the fly inside `__getitem__` and are standard for image datasets.",
            "B": "Correct. `IterableDataset` is designed for streaming or sequentially read datasets where random indexing (`dataset[idx]`) is infeasible.",
            "C": "Incorrect. `IterableDataset` has no concept of keys/indices and cannot use `DataLoader(..., shuffle=True)`.",
            "D": "Incorrect. In-memory arrays are best served by a map-style `Dataset` (such as `TensorDataset`) which supports fast random indexing."
        },
        "competency": "Distinguish use cases for Map-style Dataset vs IterableDataset",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb"
    },
    {
        "id": "PTCA-D-006",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "What is the outcome of executing the following code snippet that wraps an `IterableDataset` in a `DataLoader`?"
        ),
        "code": (
            "import torch\n"
            "from torch.utils.data import IterableDataset, DataLoader\n\n"
            "class LogStreamDataset(IterableDataset):\n"
            "    def __iter__(self):\n"
            "        for i in range(50):\n"
            "            yield torch.tensor([float(i)]), torch.tensor(i % 2)\n\n"
            "stream_ds = LogStreamDataset()\n"
            "loader = DataLoader(stream_ds, batch_size=10, shuffle=True)"
        ),
        "options": {
            "A": "It buffers all 50 items in memory, shuffles them, and yields 5 batches of size 10.",
            "B": "It shuffles only the 10 items within each individual minibatch.",
            "C": "It raises a `ValueError` because `DataLoader` with an `IterableDataset` does not support `shuffle=True`.",
            "D": "It silently ignores `shuffle=True` and yields batches in sequential order `0..49`."
        },
        "correct": ["C"],
        "explanation": (
            "Because `IterableDataset` instances have no notion of an index or key, `DataLoader` cannot apply random index "
            "sampling to shuffle them. Passing `shuffle=True` with an `IterableDataset` immediately raises "
            "`ValueError: DataLoader with IterableDataset: expected unspecified shuffle option, but got shuffle=True`."
        ),
        "option_explanations": {
            "A": "Incorrect. `DataLoader` never materializes an entire `IterableDataset` into memory to shuffle it.",
            "B": "Incorrect. `DataLoader` does not perform intra-batch shuffling when `shuffle=True` is passed to an `IterableDataset`.",
            "C": "Correct. `shuffle=True` is mutually exclusive with `IterableDataset` and raises a `ValueError` at `DataLoader` construction time.",
            "D": "Incorrect. PyTorch explicitly raises a `ValueError` rather than silently ignoring `shuffle=True`."
        },
        "competency": "Explain why DataLoader shuffle=True is incompatible with IterableDataset",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb"
    },
    {
        "id": "PTCA-D-007",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "In `modules/module_6_pytorch_nn_hands_on/pytorch_nn_linear.ipynb`, the California Housing features `X_train` "
            "and targets `Y_train` are wrapped using `torch.utils.data.TensorDataset(X_train, Y_train)`. "
            "What constraint must `X_train` and `Y_train` satisfy for `TensorDataset` to succeed?"
        ),
        "code": (
            "X_train = torch.tensor(train_data, dtype=torch.float32)          # shape: (16512, 8)\n"
            "Y_train = torch.tensor(train_target, dtype=torch.float32).view(-1, 1)  # shape: (16512, 1)\n"
            "dataset = torch.utils.data.TensorDataset(X_train, Y_train)"
        ),
        "options": {
            "A": "All tensors passed to `TensorDataset` must have the exact same shape across every dimension.",
            "B": "All tensors passed to `TensorDataset` must have the same size in their first dimension (`size(0)`).",
            "C": "All tensors passed to `TensorDataset` must have the same `dtype` (`torch.float32`).",
            "D": "`TensorDataset` only accepts 2D tensors and raises an error if a 1D or 3D tensor is passed."
        },
        "correct": ["B"],
        "explanation": (
            "`TensorDataset(*tensors)` checks ` all(tensors[0].size(0) == tensor.size(0) for tensor in tensors)`. "
            "It slices each tensor along dimension 0 when indexed (`tuple(tensor[index] for tensor in self.tensors)`), "
            "so trailing dimensions and dtypes can differ freely as long as `size(0)` (the number of samples) matches."
        ),
        "option_explanations": {
            "A": "Incorrect. Trailing dimensions can differ (here `X_train` is `(16512, 8)` while `Y_train` is `(16512, 1)`).",
            "B": "Correct. Every tensor passed to `TensorDataset` must have matching `size(0)`, otherwise an `AssertionError: Size mismatch between tensors` is raised.",
            "C": "Incorrect. Feature tensors are often `torch.float32` while classification target tensors are `torch.int64` (`torch.long`).",
            "D": "Incorrect. `TensorDataset` accepts tensors of any dimensionality (1D, 2D, 3D, 4D, etc.) as long as `size(0)` matches."
        },
        "competency": "Use TensorDataset to pair feature and target tensors for DataLoader",
        "source": "modules/module_6_pytorch_nn_hands_on/pytorch_nn_linear.ipynb"
    },
    {
        "id": "PTCA-D-008",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "Given the `TensorDataset` below with three tensors, what is returned when indexing `ds[4]`?"
        ),
        "code": (
            "import torch\n"
            "from torch.utils.data import TensorDataset\n\n"
            "images = torch.randn(20, 3, 32, 32)\n"
            "tabular = torch.randn(20, 5)\n"
            "labels = torch.randint(0, 10, (20,))\n\n"
            "ds = TensorDataset(images, tabular, labels)\n"
            "sample = ds[4]"
        ),
        "options": {
            "A": "A single concatenated 1D tensor of length `3*32*32 + 5 + 1 = 3078`.",
            "B": "A 3-tuple of tensors with shapes `(3, 32, 32)`, `(5,)`, and `()` (0D scalar).",
            "C": "A 2-tuple `(features, label)` where `features` is a list `[images[4], tabular[4]]`.",
            "D": "A `ValueError` because `TensorDataset` only accepts two arguments `(features, targets)`."
        },
        "correct": ["B"],
        "explanation": (
            "`TensorDataset` accepts an arbitrary number of tensors `*tensors` with matching `size(0)` and returns "
            "`tuple(tensor[index] for tensor in self.tensors)`. Indexing `ds[4]` slices index 4 along dim 0 of each "
            "tensor, yielding shapes `(3, 32, 32)`, `(5,)`, and `()`."
        ),
        "option_explanations": {
            "A": "Incorrect. `TensorDataset` does not flatten or concatenate the tensors.",
            "B": "Correct. Indexing returns a tuple containing the 4th slice of each input tensor.",
            "C": "Incorrect. `TensorDataset` returns a flat tuple of length equal to the number of input tensors (3 here).",
            "D": "Incorrect. `TensorDataset(*tensors)` accepts any number of tensors."
        },
        "competency": "Predict the output structure and shapes of multi-tensor TensorDataset indexing",
        "source": "LFD2001 Ch. 2"
    },
    {
        "id": "PTCA-D-009",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "Review the custom image dataset implementation below. Although it produces the correct tensors, training "
            "is extremely slow and disk I/O is saturated on every step. What is the root cause of this performance bug?"
        ),
        "code": (
            "import pandas as pd\n"
            "from PIL import Image\n"
            "from torch.utils.data import Dataset\n\n"
            "class DefectDataset(Dataset):\n"
            "    def __init__(self, csv_path, transform=None):\n"
            "        self.csv_path = csv_path\n"
            "        self.transform = transform\n\n"
            "    def __len__(self):\n"
            "        return len(pd.read_csv(self.csv_path))\n\n"
            "    def __getitem__(self, idx):\n"
            "        df = pd.read_csv(self.csv_path)\n"
            "        row = df.iloc[idx]\n"
            "        img = Image.open(row['image_path']).convert('RGB')\n"
            "        if self.transform:\n"
            "            img = self.transform(img)\n"
            "        return img, int(row['label'])"
        ),
        "options": {
            "A": "`Image.open()` should be called on all images inside `__init__` and stored as uncompressed float64 tensors in RAM.",
            "B": "`pd.read_csv(self.csv_path)` is being re-parsed from disk on every single `__getitem__` and `__len__` call instead of being loaded once in `__init__`.",
            "C": "`self.transform` should be applied inside `__len__` rather than `__getitem__`.",
            "D": "Subclassing `Dataset` forces single-threaded execution; only `TensorDataset` can read CSV files efficiently."
        },
        "correct": ["B"],
        "explanation": (
            "In a map-style `Dataset`, lightweight metadata such as the annotations CSV (`pd.read_csv(csv_path)`) should "
            "be loaded once in `__init__` and stored in `self.annotations`, while `__getitem__(self, idx)` lazily loads "
            "only the `idx`-th image file. Re-reading the entire CSV file on every sample access creates an $O(N^2)$ I/O bottleneck."
        ),
        "option_explanations": {
            "A": "Incorrect. Loading all images into RAM in `__init__` can cause out-of-memory crashes on large image datasets; lazy image loading in `__getitem__` is standard.",
            "B": "Correct. Parsing the metadata CSV on every `__getitem__` and `__len__` call wastes massive disk I/O and CPU time.",
            "C": "Incorrect. `__len__` only returns an integer sample count and never processes images.",
            "D": "Incorrect. Custom `Dataset` subclasses support multi-process loading via `num_workers`."
        },
        "competency": "Identify anti-patterns in __init__ vs __getitem__ resource loading in custom Datasets",
        "source": "LFD2001 Ch. 2"
    },
    {
        "id": "PTCA-D-010",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "In `pytorch_data_utilities.ipynb`, the code below is used to visualize a sample from `FashionMNIST` with "
            "`matplotlib.pyplot.imshow`. Why is `.squeeze()` called on `img` before passing it to `plt.imshow()`?"
        ),
        "code": (
            "img, label = training_data[sample_idx]\n"
            "plt.imshow(img.squeeze(), cmap='gray')"
        ),
        "options": {
            "A": "Because `ToTensor()` outputs a tensor of shape `(1, 28, 28)` with channel-first ordering, whereas `plt.imshow` expects a 2D grayscale array `(28, 28)` or channel-last `(H, W, C)`.",
            "B": "Because `training_data[sample_idx]` returns a 4D minibatch tensor `(1, 1, 28, 28)` and `.squeeze()` removes only the batch dimension.",
            "C": "Because `.squeeze()` rescales pixel values from `[0.0, 1.0]` back to `[0, 255]` integers.",
            "D": "Because `.squeeze()` detaches the tensor from the autograd computation graph."
        },
        "correct": ["A"],
        "explanation": (
            "In PyTorch, grayscale images transformed by `ToTensor()` have shape `(C, H, W) = (1, 28, 28)`. Matplotlib's "
            "`plt.imshow()` accepts `(H, W)` for grayscale or `(H, W, 3)`/`(H, W, 4)` for RGB/RGBA, and rejects `(1, 28, 28)`. "
            "Calling `img.squeeze()` removes the size-1 channel dimension, producing shape `(28, 28)`."
        ),
        "option_explanations": {
            "A": "Correct. `.squeeze()` removes the leading size-1 channel dimension so `plt.imshow` receives a 2D `(28, 28)` tensor.",
            "B": "Incorrect. Indexing a `Dataset` returns a 3D `(1, 28, 28)` image tensor, not a 4D batch tensor.",
            "C": "Incorrect. `.squeeze()` only removes dimensions of size 1; it does not alter tensor values or dtype.",
            "D": "Incorrect. `.squeeze()` returns a view of the tensor and does not detach gradients (nor do dataset tensors require grad by default)."
        },
        "competency": "Reconcile PyTorch (C, H, W) image tensor conventions with visualization tools",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb"
    },
    {
        "id": "PTCA-D-011",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "You have two map-style datasets, `factory_a_ds` (1,200 samples) and `factory_b_ds` (800 samples), that "
            "return identically formatted `(image_tensor, label_int)` tuples. Which `torch.utils.data` utility combines "
            "them into a single unified map-style dataset of 2,000 samples without copying the underlying data in memory?"
        ),
        "code": (
            "from torch.utils.data import ConcatDataset, ChainDataset, Subset\n\n"
            "# Combine factory_a_ds (len=1200) and factory_b_ds (len=800)"
        ),
        "options": {
            "A": "`ConcatDataset([factory_a_ds, factory_b_ds])`",
            "B": "`ChainDataset([factory_a_ds, factory_b_ds])`",
            "C": "`Subset(factory_a_ds, factory_b_ds)`",
            "D": "`torch.cat([factory_a_ds, factory_b_ds], dim=0)`"
        },
        "correct": ["A"],
        "explanation": (
            "`torch.utils.data.ConcatDataset(datasets)` takes a sequence of map-style `Dataset` objects and routes index "
            "lookups `combined[idx]` across cumulative lengths (`1200 + 800 = 2000`). By contrast, `ChainDataset` is "
            "strictly for chaining `IterableDataset` instances and raises an assertion error on map-style datasets."
        ),
        "option_explanations": {
            "A": "Correct. `ConcatDataset` virtually concatenates multiple map-style datasets while preserving random access and `__len__`.",
            "B": "Incorrect. `ChainDataset` only accepts `IterableDataset` subclasses and does not support random indexing.",
            "C": "Incorrect. `Subset(dataset, indices)` selects a subset of indices from a single dataset.",
            "D": "Incorrect. `torch.cat` operates on `torch.Tensor` objects, not `Dataset` instances."
        },
        "competency": "Combine multiple map-style datasets using ConcatDataset",
        "source": "LFD2001 Ch. 2"
    },
    {
        "id": "PTCA-D-012",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "Suppose `full_ds` is a map-style dataset of 1,000 samples where `full_ds[i]` returns `i * 10`. "
            "What is the output of the code below using `torch.utils.data.Subset`?"
        ),
        "code": (
            "from torch.utils.data import Subset\n\n"
            "indices = [5, 12, 30, 100]\n"
            "sub_ds = Subset(full_ds, indices)\n"
            "print(len(sub_ds), sub_ds[2])"
        ),
        "options": {
            "A": "`1000 20`",
            "B": "`4 300`",
            "C": "`4 20`",
            "D": "`IndexError: index 2 is not in [5, 12, 30, 100]`"
        },
        "correct": ["B"],
        "explanation": (
            "`Subset(dataset, indices)` creates a map-style dataset view whose length is `len(indices)` (`4`) and where "
            "`sub_ds[idx]` delegates to `dataset[self.indices[idx]]`. Thus `sub_ds[2]` accesses `full_ds[indices[2]] = full_ds[30] = 300`."
        ),
        "option_explanations": {
            "A": "Incorrect. `len(sub_ds)` equals the number of selected indices (`4`), and `sub_ds[2]` maps through `indices[2]`, not directly to `full_ds[2]`.",
            "B": "Correct. `len(sub_ds)` is `4`, and `sub_ds[2]` retrieves `full_ds[indices[2]] = full_ds[30] = 300`.",
            "C": "Incorrect. `sub_ds[2]` looks up the 3rd element of `indices` (`30`), not index `2` of `full_ds`.",
            "D": "Incorrect. `Subset` re-indexes its elements from `0` to `len(indices) - 1`."
        },
        "competency": "Use torch.utils.data.Subset to create indexed views of a Dataset",
        "source": "LFD2001 Ch. 2"
    },
    {
        "id": "PTCA-D-013",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Hard",
        "multi_select": False,
        "stem": (
            "A custom dataset loads RGB and grayscale images from a mixed directory using `PIL.Image.open(path)` without "
            "calling `.convert('RGB')`, and then applies `transforms.ToTensor()` and `transforms.Resize((64, 64))`. "
            "When iterating over `DataLoader(ds, batch_size=8)`, what error occurs when a batch contains seven RGB images "
            "and one single-channel grayscale image?"
        ),
        "code": (
            "class MixedFolderDataset(Dataset):\n"
            "    def __init__(self, paths):\n"
            "        self.paths = paths\n"
            "        self.tf = transforms.Compose([transforms.Resize((64, 64)), transforms.ToTensor()])\n"
            "    def __len__(self):\n"
            "        return len(self.paths)\n"
            "    def __getitem__(self, idx):\n"
            "        return self.tf(Image.open(self.paths[idx]))"
        ),
        "options": {
            "A": "`ToTensor()` automatically broadcasts 1-channel grayscale images to 3 channels, so no error occurs.",
            "B": "`default_collate` raises a `RuntimeError: stack expects each tensor to be equal size, but got [3, 64, 64] at entry 0 and [1, 64, 64] at entry ...`.",
            "C": "`DataLoader` drops the grayscale image and yields a batch of size 7.",
            "D": "`PIL.Image.open` raises an `OSError` when opening a grayscale image alongside RGB images."
        },
        "correct": ["B"],
        "explanation": (
            "A grayscale PIL image (`mode='L'`) is converted by `ToTensor()` to shape `(1, 64, 64)`, whereas an RGB PIL "
            "image (`mode='RGB'`) becomes `(3, 64, 64)`. When `DataLoader`'s `default_collate` tries to `torch.stack` "
            "the 8 sample tensors into a batch, the mismatched channel dimension triggers a `RuntimeError`."
        ),
        "option_explanations": {
            "A": "Incorrect. `ToTensor()` preserves the number of channels in the input PIL image (1 for `'L'`, 3 for `'RGB'`, 4 for `'RGBA'`).",
            "B": "Correct. `torch.stack` inside `default_collate` requires all tensors in the batch to have identical shapes across all dimensions, including channels.",
            "C": "Incorrect. `DataLoader` never silently drops mismatched samples.",
            "D": "Incorrect. `Image.open` opens grayscale images without error; the failure happens during batch collation."
        },
        "competency": "Debug shape mismatch RuntimeErrors caused by inconsistent channel counts in custom Datasets",
        "source": "LFD2001 Ch. 2"
    },
    {
        "id": "PTCA-D-014",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "In `modules/module_6_pytorch_nn_hands_on/pytorch_nn_linear.ipynb`, why is the NumPy array `train_data` "
            "from `sklearn.datasets.fetch_california_housing()` explicitly converted with `dtype=torch.float32` and why "
            "is `train_target` reshaped with `.view(-1, 1)` before creating the `TensorDataset`?"
        ),
        "code": (
            "X_train = torch.tensor(train_data, dtype=torch.float32)\n"
            "Y_train = torch.tensor(train_target, dtype=torch.float32).view(-1, 1)"
        ),
        "options": {
            "A": "Because `scikit-learn` arrays default to `float64` while `nn.Linear` parameters default to `float32`, and `.view(-1, 1)` matches the `(batch_size, 1)` output shape of `nn.Linear(hidden_dim, 1)` in `MSELoss`.",
            "B": "Because `TensorDataset` rejects `float64` tensors and requires 2D tensors with at least 1 column.",
            "C": "Because `torch.tensor()` defaults to `int64` when converting NumPy floating-point arrays.",
            "D": "Because `nn.ReLU()` only operates on 2D `float32` column vectors."
        },
        "correct": ["A"],
        "explanation": (
            "NumPy floating-point arrays from `scikit-learn` have `dtype=np.float64` (`torch.float64`), which causes a "
            "`RuntimeError: mat1 and mat2 must have the same dtype, but got Double and Float` when passed to a default "
            "`nn.Linear` layer (`float32`). Furthermore, `train_target` has 1D shape `(N,)`, so `.view(-1, 1)` reshapes "
            "it to `(N, 1)` so each minibatch `Y` has shape `(batch_size, 1)` matching `model(X)` in `MSELoss(outputs, Y)` "
            "without unintended `(batch_size, batch_size)` broadcasting."
        ),
        "option_explanations": {
            "A": "Correct. Matching `float32` prevents dtype mismatch in `nn.Linear`, and `.view(-1, 1)` aligns target shape `(B, 1)` with model predictions `(B, 1)`.",
            "B": "Incorrect. `TensorDataset` accepts any tensor dtype and 1D shapes.",
            "C": "Incorrect. `torch.tensor()` infers `torch.float64` from a `np.float64` array, not `int64`.",
            "D": "Incorrect. `nn.ReLU()` works on tensors of any shape and floating-point dtype."
        },
        "competency": "Prepare external NumPy/scikit-learn datasets with proper dtype and shape for PyTorch models",
        "source": "modules/module_6_pytorch_nn_hands_on/pytorch_nn_linear.ipynb"
    },
    {
        "id": "PTCA-D-015",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "You have a directory of images organized into class subfolders (`data/train/cat/*.jpg`, `data/train/dog/*.jpg`) "
            "and load it with `ds = torchvision.datasets.ImageFolder(root='data/train', transform=ToTensor())`. "
            "Which attributes on `ds` provide (1) the ordered list of class names and (2) the dictionary mapping each "
            "class name to its integer label index?"
        ),
        "code": (
            "from torchvision import datasets\n"
            "from torchvision.transforms import ToTensor\n\n"
            "ds = datasets.ImageFolder(root='data/train', transform=ToTensor())"
        ),
        "options": {
            "A": "`ds.labels` and `ds.label_map`",
            "B": "`ds.classes` and `ds.class_to_idx`",
            "C": "`ds.categories` and `ds.cat2idx`",
            "D": "`ds.target_names` and `ds.target_dict`"
        },
        "correct": ["B"],
        "explanation": (
            "Standard `torchvision.datasets` classification datasets (including `ImageFolder`, `FashionMNIST`, `MNIST`, "
            "and `CIFAR10`) expose `ds.classes` (a list of class name strings sorted alphabetically in `ImageFolder`) "
            "and `ds.class_to_idx` (a dict mapping `{class_name: int_index}`)."
        ),
        "option_explanations": {
            "A": "Incorrect. Neither `labels` nor `label_map` is the standard attribute for class names/mappings in `ImageFolder`.",
            "B": "Correct. `ds.classes` holds the list of class names and `ds.class_to_idx` maps class names to integer indices.",
            "C": "Incorrect. `categories` and `cat2idx` do not exist on `ImageFolder`.",
            "D": "Incorrect. `target_names` is a `scikit-learn` convention (e.g., `fetch_california_housing`), not `torchvision.datasets`."
        },
        "competency": "Inspect class names and label-to-index mappings in torchvision datasets",
        "source": "LFD2001 Ch. 2"
    },
    {
        "id": "PTCA-D-016",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "A custom `Dataset.__getitem__` returns `(feature_tensor, label)` where `label` is `int(row['class_id'])` "
            "for valid rows, but returns `None` when `row['class_id']` is missing (`NaN`). What happens when `DataLoader` "
            "attempts to collate a batch containing a sample whose label is `None`?"
        ),
        "code": (
            "class NoisyLabelDataset(Dataset):\n"
            "    def __init__(self, x, y):\n"
            "        self.x = x\n"
            "        self.y = y  # e.g. [0, 1, None, 1]\n"
            "    def __len__(self):\n"
            "        return len(self.x)\n"
            "    def __getitem__(self, idx):\n"
            "        return self.x[idx], self.y[idx]"
        ),
        "options": {
            "A": "`default_collate` replaces `None` with `-100` (`ignore_index`) automatically.",
            "B": "`default_collate` raises a `TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'NoneType'>`.",
            "C": "`DataLoader` automatically skips any sample tuple containing `None`.",
            "D": "`default_collate` converts `None` into `float('nan')` inside a `torch.float32` label tensor."
        },
        "correct": ["B"],
        "explanation": (
            "PyTorch's `default_collate` only knows how to collate `torch.Tensor`, NumPy arrays, Python numbers (`int`, `float`), "
            "strings, mappings (`dict`), and sequences (`list`, `tuple`). Encountering `None` (`NoneType`) inside a sample "
            "raises a `TypeError` unless a custom `collate_fn` filters or handles `None`."
        ),
        "option_explanations": {
            "A": "Incorrect. `default_collate` never substitutes `-100` for `None`.",
            "B": "Correct. `NoneType` is not supported by `default_collate` and triggers a `TypeError`.",
            "C": "Incorrect. `DataLoader` does not filter out `None` values unless a custom `collate_fn` is provided.",
            "D": "Incorrect. `default_collate` does not coerce `None` to `NaN`."
        },
        "competency": "Diagnose TypeError in default_collate when __getitem__ returns unsupported Python types",
        "source": "LFD2001 Ch. 2"
    },
    {
        "id": "PTCA-D-017",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "What happens if a custom `Dataset.__getitem__(self, idx)` returns a dictionary "
            "`{'features': torch.randn(10), 'target': torch.tensor(1)}` and you iterate over `DataLoader(ds, batch_size=32)`?"
        ),
        "code": (
            "class DictDataset(Dataset):\n"
            "    def __len__(self):\n"
            "        return 64\n"
            "    def __getitem__(self, idx):\n"
            "        return {'features': torch.randn(10), 'target': torch.tensor(idx % 2)}\n\n"
            "loader = DataLoader(DictDataset(), batch_size=32)\n"
            "batch = next(iter(loader))"
        ),
        "options": {
            "A": "`DataLoader` raises a `TypeError` because `__getitem__` must return a tuple, not a dictionary.",
            "B": "`batch` is a list of 32 individual dictionaries.",
            "C": "`batch` is a single dictionary `{'features': Tensor(32, 10), 'target': Tensor(32)}` where values are collated per key.",
            "D": "`batch` is a 2-tuple of keys `('features', 'target')` and the tensor values are discarded."
        },
        "correct": ["C"],
        "explanation": (
            "`default_collate` recursively handles `collections.abc.Mapping` (such as `dict`) by collating the values "
            "for each key across the batch list: `{key: default_collate([d[key] for d in batch]) for key in elem}`. "
            "Therefore, `batch` is a single dictionary mapping `'features'` to a `(32, 10)` tensor and `'target'` to a `(32,)` tensor."
        ),
        "option_explanations": {
            "A": "Incorrect. `default_collate` natively supports dictionaries, tuples, lists, namedtuples, tensors, and numbers.",
            "B": "Incorrect. `default_collate` merges the 32 dicts into a single dict of batched tensors rather than leaving them as a list of dicts.",
            "C": "Correct. `default_collate` preserves the dictionary structure and stacks the tensor values for each key.",
            "D": "Incorrect. Iterating over a dict alone yields keys, but `default_collate` specifically inspects mappings and collates their values."
        },
        "competency": "Predict how default_collate batches dictionary and nested sample structures from a Dataset",
        "source": "LFD2001 Ch. 2"
    },
    {
        "id": "PTCA-D-018",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Hard",
        "multi_select": False,
        "stem": (
            "Consider the custom `Dataset` below that caches preprocessed tensors in a Python `dict` (`self.cache`) "
            "inside `__getitem__`. When used with `DataLoader(ds, batch_size=32, num_workers=4)` without `persistent_workers=True`, "
            "why is the cache rebuilt at the start of every single epoch?"
        ),
        "code": (
            "class CachedDataset(Dataset):\n"
            "    def __init__(self, file_paths):\n"
            "        self.file_paths = file_paths\n"
            "        self.cache = {}\n"
            "    def __len__(self):\n"
            "        return len(self.file_paths)\n"
            "    def __getitem__(self, idx):\n"
            "        if idx not in self.cache:\n"
            "            self.cache[idx] = expensive_load(self.file_paths[idx])\n"
            "        return self.cache[idx]"
        ),
        "options": {
            "A": "Because `DataLoader` calls `ds.__init__()` at the beginning of each epoch.",
            "B": "Because each worker process receives its own copy of `CachedDataset`, mutates only its own process-local `self.cache`, and worker processes are terminated and respawned at each epoch boundary when `persistent_workers=False`.",
            "C": "Because Python dictionaries are automatically cleared by `torch.cuda.empty_cache()` after each epoch.",
            "D": "Because `RandomSampler` deletes keys from `self.cache` as indices are consumed."
        },
        "correct": ["B"],
        "explanation": (
            "With `num_workers > 0`, `DataLoader` spawns separate worker processes that each get a copy of `CachedDataset`. "
            "A plain Python `dict` (`self.cache`) is not shared across processes, so mutations in workers never update the "
            "main process's `ds.cache`. Furthermore, by default (`persistent_workers=False`), worker processes are shut "
            "down at the end of every epoch and freshly spawned at the next epoch, discarding their process-local caches."
        ),
        "option_explanations": {
            "A": "Incorrect. `DataLoader` never re-invokes `ds.__init__()`.",
            "B": "Correct. Worker processes have isolated memory spaces for plain Python dicts and are destroyed at the end of each epoch unless `persistent_workers=True` or shared memory is used.",
            "C": "Incorrect. `torch.cuda.empty_cache()` only releases unused cached GPU memory blocks to the CUDA driver.",
            "D": "Incorrect. `RandomSampler` only generates integer indices and never accesses `ds.cache`."
        },
        "competency": "Understand multiprocessing memory isolation in custom Dataset state when num_workers > 0",
        "source": "LFD2001 Ch. 2 & Ch. 3"
    },
    {
        "id": "PTCA-D-019",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "In `pytorch_data_utilities.ipynb`, when loading `datasets.FashionMNIST(root='data', train=True, download=True, transform=ToTensor())`, "
            "what happens if the FashionMNIST files have ALREADY been downloaded and extracted inside the `'data'` directory "
            "from a previous run?"
        ),
        "code": (
            "training_data = datasets.FashionMNIST(\n"
            "    root='data',\n"
            "    train=True,\n"
            "    download=True,\n"
            "    transform=ToTensor()\n"
            ")"
        ),
        "options": {
            "A": "It raises a `FileExistsError` unless `download=False` is set on subsequent runs.",
            "B": "It deletes the `'data'` directory and re-downloads the archive from the internet every time.",
            "C": "It verifies that the dataset files already exist at `root` and loads them from local disk without re-downloading.",
            "D": "It creates a duplicate directory `'data_1'` and downloads a fresh copy there."
        },
        "correct": ["C"],
        "explanation": (
            "As documented in `pytorch_data_utilities.ipynb`, the `download=True` parameter downloads the dataset from "
            "the internet only if it is not already available at `root`. If the files are already present and pass integrity "
            "checks, TorchVision skips the download and loads them directly from disk."
        ),
        "option_explanations": {
            "A": "Incorrect. `download=True` is idempotent and does not raise `FileExistsError` when files already exist.",
            "B": "Incorrect. Existing valid files are reused rather than deleted and re-downloaded.",
            "C": "Correct. `download=True` checks for existing files at `root` first and only downloads if they are missing.",
            "D": "Incorrect. TorchVision never creates numbered duplicate directories."
        },
        "competency": "Configure torchvision dataset root and download parameters",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb"
    },
    {
        "id": "PTCA-D-020",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "A developer writes an `IterableDataset` subclass as shown below. What happens when `next(iter(DataLoader(ds, batch_size=4)))` "
            "is executed?"
        ),
        "code": (
            "import torch\n"
            "from torch.utils.data import IterableDataset, DataLoader\n\n"
            "class BrokenStream(IterableDataset):\n"
            "    def __init__(self, data):\n"
            "        self.data = data\n"
            "    def __len__(self):\n"
            "        return len(self.data)\n"
            "    def __getitem__(self, idx):\n"
            "        return self.data[idx]\n\n"
            "ds = BrokenStream(torch.arange(20))\n"
            "batch = next(iter(DataLoader(ds, batch_size=4)))"
        ),
        "options": {
            "A": "It returns `tensor([0, 1, 2, 3])` because `IterableDataset` falls back to `__getitem__` when `__iter__` is omitted.",
            "B": "It raises a `NotImplementedError` because `IterableDataset` requires subclasses to override `__iter__(self)`.",
            "C": "It returns a single scalar `tensor(0)` because `IterableDataset` ignores `batch_size`.",
            "D": "It raises a `ValueError` because `IterableDataset` forbids defining `__len__`."
        },
        "correct": ["B"],
        "explanation": (
            "Unlike Python's general `iter(obj)` which falls back to `__getitem__(0, 1, ...)` if `__iter__` is absent, "
            "`torch.utils.data.IterableDataset` explicitly defines `def __iter__(self): raise NotImplementedError`. "
            "Subclassing `IterableDataset` without overriding `__iter__` therefore raises `NotImplementedError` on iteration."
        ),
        "option_explanations": {
            "A": "Incorrect. `IterableDataset` defines a stub `__iter__` that raises `NotImplementedError`, preventing Python's `__getitem__` fallback.",
            "B": "Correct. Subclasses of `IterableDataset` must implement `__iter__(self)`.",
            "C": "Incorrect. `IterableDataset` supports `batch_size` via `_IterableDatasetFetcher`, and fails here due to missing `__iter__`.",
            "D": "Incorrect. An `IterableDataset` may optionally implement `__len__` (though it must return an accurate count if used)."
        },
        "competency": "Implement the __iter__ contract required by torch.utils.data.IterableDataset",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb & LFD2001 Ch. 2"
    },
    {
        "id": "PTCA-D-021",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "In a custom map-style `Dataset` for a multi-class classification task using `nn.CrossEntropyLoss()`, "
            "what tensor `dtype` and shape should each individual sample's target label have when returned by `__getitem__` "
            "(assuming standard class-index targets rather than soft probabilities)?"
        ),
        "code": (
            "class CustomClassifierDataset(Dataset):\n"
            "    def __init__(self, features, labels):\n"
            "        self.features = features\n"
            "        self.labels = labels\n"
            "    def __len__(self):\n"
            "        return len(self.features)\n"
            "    def __getitem__(self, idx):\n"
            "        x = torch.tensor(self.features[idx], dtype=torch.float32)\n"
            "        y = # How should the class index label be returned?\n"
            "        return x, y"
        ),
        "options": {
            "A": "A 0D scalar `torch.int64` (`torch.long`) tensor (or Python `int`), which collates to a 1D `(batch_size,)` `torch.long` tensor.",
            "B": "A 2D `(1, 1)` `torch.float32` tensor, which collates to `(batch_size, 1, 1)`.",
            "C": "A 1D `(1,)` `torch.int32` (`torch.int`) tensor, which collates to `(batch_size, 1)` of `int32`.",
            "D": "A 0D scalar `torch.uint8` tensor, because `nn.CrossEntropyLoss` only accepts unsigned 8-bit integer targets."
        },
        "correct": ["A"],
        "explanation": (
            "`nn.CrossEntropyLoss` expects class-index targets for a minibatch of $B$ samples to be a 1D tensor of shape "
            "`(B,)` with `dtype=torch.long` (`torch.int64`). Returning a 0D `torch.long` scalar tensor (or a Python `int`, "
            "which `default_collate` converts to a `torch.int64` tensor) from `__getitem__` stacks cleanly into shape `(B,)`."
        ),
        "option_explanations": {
            "A": "Correct. A 0D `torch.long` tensor or Python `int` per sample collates into a 1D `(batch_size,)` `torch.long` tensor required by `nn.CrossEntropyLoss`.",
            "B": "Incorrect. `nn.CrossEntropyLoss` rejects 3D `(B, 1, 1)` float32 class-index targets.",
            "C": "Incorrect. `nn.CrossEntropyLoss` requires 1D `(B,)` targets of `dtype=torch.long` (`int64`), and rejects `(B, 1)` or `int32`.",
            "D": "Incorrect. `torch.uint8` is not accepted as a class index target by `nn.CrossEntropyLoss`."
        },
        "competency": "Return appropriately typed and shaped labels from custom Datasets for classification losses",
        "source": "LFD2001 Ch. 2"
    },
    {
        "id": "PTCA-D-022",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D1,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "What happens when a user slices a `TensorDataset` directly using Python slice syntax `ds[10:25]` vs indexing "
            "a single integer `ds[10]`?"
        ),
        "code": (
            "import torch\n"
            "from torch.utils.data import TensorDataset\n\n"
            "X = torch.randn(100, 4)\n"
            "Y = torch.arange(100)\n"
            "ds = TensorDataset(X, Y)\n\n"
            "single = ds[10]\n"
            "sliced = ds[10:25]"
        ),
        "options": {
            "A": "`ds[10:25]` raises a `TypeError` because `Dataset` subclasses do not support slice objects.",
            "B": "`ds[10:25]` returns a list of 15 two-tuples `[(X[10], Y[10]), ..., (X[24], Y[24])]`.",
            "C": "`ds[10:25]` returns a single two-tuple `(X[10:25], Y[10:25])` where `X[10:25]` has shape `(15, 4)` and `Y[10:25]` has shape `(15,)`.",
            "D": "`ds[10:25]` returns a new `Subset(ds, range(10, 25))` instance."
        },
        "correct": ["C"],
        "explanation": (
            "`TensorDataset.__getitem__(self, index)` simply executes `tuple(tensor[index] for tensor in self.tensors)`. "
            "When `index` is a slice `10:25`, each underlying tensor is sliced directly along dimension 0, returning a "
            "single tuple of sliced tensors `(X[10:25], Y[10:25])` with shapes `(15, 4)` and `(15,)`."
        ),
        "option_explanations": {
            "A": "Incorrect. Because `TensorDataset` forwards `index` directly to tensor indexing, slice objects work natively.",
            "B": "Incorrect. It returns a tuple of sliced tensors, not a list of per-sample tuples.",
            "C": "Correct. `tuple(tensor[10:25] for tensor in self.tensors)` yields a 2-tuple of tensors with leading dimension 15.",
            "D": "Incorrect. Slicing a `TensorDataset` returns tensors, not a `Subset` object."
        },
        "competency": "Understand TensorDataset indexing and slicing behavior",
        "source": "LFD2001 Ch. 2"
    },

    # =========================================================================
    # D2: DataLoader Configuration, Batching, Sampling & Performance
    # (PTCA-D-023 to PTCA-D-050, 28 questions)
    # =========================================================================
    {
        "id": "PTCA-D-023",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "If you instantiate `loader = torch.utils.data.DataLoader(dataset)` passing ONLY the required `dataset` "
            "argument, what are the default values of `batch_size`, `shuffle`, `num_workers`, `pin_memory`, and `drop_last`?"
        ),
        "code": (
            "from torch.utils.data import DataLoader\n\n"
            "loader = DataLoader(dataset)"
        ),
        "options": {
            "A": "`batch_size=32, shuffle=True, num_workers=1, pin_memory=False, drop_last=False`",
            "B": "`batch_size=1, shuffle=False, num_workers=0, pin_memory=False, drop_last=False`",
            "C": "`batch_size=None, shuffle=False, num_workers=0, pin_memory=True, drop_last=False`",
            "D": "`batch_size=64, shuffle=False, num_workers=0, pin_memory=False, drop_last=True`"
        },
        "correct": ["B"],
        "explanation": (
            "As documented in `pytorch_data_utilities.ipynb` and the PyTorch API, `dataset` is the only required argument "
            "for `DataLoader`, and its default parameters are `batch_size=1`, `shuffle=False`, `num_workers=0` (load in "
            "the main process), `pin_memory=False`, and `drop_last=False`."
        ),
        "option_explanations": {
            "A": "Incorrect. `DataLoader` defaults to `batch_size=1`, `shuffle=False`, and `num_workers=0`.",
            "B": "Correct. All five default parameter values match the `torch.utils.data.DataLoader` signature.",
            "C": "Incorrect. `batch_size` defaults to `1` (not `None`), and `pin_memory` defaults to `False`.",
            "D": "Incorrect. `batch_size=64` is used in the notebook's example, not as the constructor default, and `drop_last` defaults to `False`."
        },
        "competency": "Recall required and default parameters of torch.utils.data.DataLoader",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb"
    },
    {
        "id": "PTCA-D-024",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "A map-style dataset contains $N = 1,050$ samples. You create two DataLoaders:\n"
            "`loader_keep = DataLoader(dataset, batch_size=64, drop_last=False)`\n"
            "`loader_drop = DataLoader(dataset, batch_size=64, drop_last=True)`\n"
            "What are `len(loader_keep)`, the size of the final batch in `loader_keep`, and `len(loader_drop)`?"
        ),
        "code": (
            "loader_keep = DataLoader(dataset, batch_size=64, drop_last=False)\n"
            "loader_drop = DataLoader(dataset, batch_size=64, drop_last=True)"
        ),
        "options": {
            "A": "`len(loader_keep) = 16`, final batch size `= 26`, `len(loader_drop) = 16`",
            "B": "`len(loader_keep) = 17`, final batch size `= 26`, `len(loader_drop) = 16`",
            "C": "`len(loader_keep) = 17`, final batch size `= 64`, `len(loader_drop) = 16`",
            "D": "`len(loader_keep) = 16`, final batch size `= 50`, `len(loader_drop) = 15`"
        },
        "correct": ["B"],
        "explanation": (
            "Since $1050 = 16 \\times 64 + 26$, with `drop_last=False` the number of batches is "
            "$\\lceil 1050 / 64 \\rceil = 17$, and the 17th (final) batch contains the remaining $1050 \\pmod{64} = 26$ samples. "
            "With `drop_last=True`, the incomplete final batch is dropped, leaving $\\lfloor 1050 / 64 \\rfloor = 16$ full batches of 64."
        ),
        "option_explanations": {
            "A": "Incorrect. `loader_keep` includes the partial 17th batch of 26 samples, so `len(loader_keep)` is 17.",
            "B": "Correct. $16 \\times 64 = 1024$ with remainder $26$, giving 17 batches (last of size 26) when `drop_last=False` and 16 batches when `drop_last=True`.",
            "C": "Incorrect. `DataLoader` does not pad or duplicate samples to make the final batch size 64.",
            "D": "Incorrect. $1050 / 64 = 16$ remainder $26$, not $15$ remainder $50$."
        },
        "competency": "Calculate batch counts and remainder batch sizes with drop_last=False vs drop_last=True",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-025",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "A neural network contains `nn.BatchNorm1d(128)` layers and is trained in `model.train()` mode on a dataset "
            "of $N = 1,025$ samples with `DataLoader(train_ds, batch_size=32, shuffle=True, drop_last=False)`. "
            "At the very last step of the first epoch, training crashes with:\n"
            "`ValueError: Expected more than 1 value per channel when training, got input size torch.Size([1, 128])`.\n"
            "What is the cleanest `DataLoader` configuration change to prevent this crash during training?"
        ),
        "code": (
            "# len(train_ds) == 1025\n"
            "train_loader = DataLoader(train_ds, batch_size=32, shuffle=True, drop_last=False)"
        ),
        "options": {
            "A": "Set `drop_last=True` in `train_loader` so the trailing 1-sample batch ($1025 \\pmod{32} = 1$) is dropped each shuffled epoch.",
            "B": "Set `pin_memory=True` in `train_loader` so the final sample is padded in CUDA memory.",
            "C": "Switch the model to `model.eval()` during the entire training loop.",
            "D": "Set `shuffle=False` in `train_loader` so the remainder batch has 32 samples."
        },
        "correct": ["A"],
        "explanation": (
            "Because $1025 = 32 \\times 32 + 1$, the final batch of each epoch has only 1 sample (`shape: [1, 128]`). "
            "`nn.BatchNorm1d` in training mode computes per-channel batch variance across the batch dimension, which "
            "requires at least 2 elements per channel. Setting `drop_last=True` drops the 1-sample remainder batch, and "
            "since `shuffle=True` reshuffles every epoch, all samples still participate in training across epochs."
        ),
        "option_explanations": {
            "A": "Correct. `drop_last=True` discards the incomplete 1-sample final batch that causes `BatchNorm1d` to fail in `train()` mode.",
            "B": "Incorrect. `pin_memory=True` affects host memory allocation, not batch sizes.",
            "C": "Incorrect. Running in `model.eval()` disables dropout and batch statistics updates during training.",
            "D": "Incorrect. `shuffle=False` does not change the remainder $1025 \\pmod{32} = 1$."
        },
        "competency": "Recognize when drop_last=True is needed for BatchNorm or fixed-batch-shape training",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-026",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "In `pytorch_data_utilities.ipynb`, how do you retrieve a single minibatch `(train_features, train_labels)` "
            "from `train_dataloader` for quick inspection outside a `for` loop?"
        ),
        "code": (
            "train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)\n"
            "# Retrieve the first batch:"
        ),
        "options": {
            "A": "`train_features, train_labels = train_dataloader[0]`",
            "B": "`train_features, train_labels = next(train_dataloader)`",
            "C": "`train_features, train_labels = next(iter(train_dataloader))`",
            "D": "`train_features, train_labels = train_dataloader.get_batch(0)`"
        },
        "correct": ["C"],
        "explanation": (
            "`DataLoader` is a Python *iterable* (it implements `__iter__`), not an *iterator* (it does not implement "
            "`__next__` directly) and not subscriptable (it does not implement `__getitem__`). Calling `iter(train_dataloader)` "
            "creates a `_SingleProcessDataLoaderIter` or `_MultiProcessingDataLoaderIter`, and `next(...)` fetches the first batch."
        ),
        "option_explanations": {
            "A": "Incorrect. `DataLoader` is not subscriptable; `train_dataloader[0]` raises `TypeError: 'DataLoader' object is not subscriptable`.",
            "B": "Incorrect. `DataLoader` is an iterable, not an iterator; `next(train_dataloader)` raises `TypeError: 'DataLoader' object is not an iterator`.",
            "C": "Correct. `next(iter(train_dataloader))` obtains an iterator from the `DataLoader` and retrieves its first batch.",
            "D": "Incorrect. `DataLoader` has no `.get_batch()` method."
        },
        "competency": "Retrieve a single batch from a DataLoader using iter() and next()",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb"
    },
    {
        "id": "PTCA-D-027",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "According to `pytorch_data_utilities.ipynb`, what is the primary reason for setting `shuffle=True` on the "
            "training `DataLoader`, and what is standard practice for `shuffle` on validation and test `DataLoader`s?"
        ),
        "code": "",
        "options": {
            "A": "`shuffle=True` in training prevents the model from memorizing sample order and reduces overfitting across epochs; validation/test loaders typically use `shuffle=False` for deterministic, reproducible evaluation.",
            "B": "`shuffle=True` in training speeds up disk reads via random seek; validation/test loaders must use `shuffle=True` to compute accurate mean loss.",
            "C": "`shuffle=True` is required for `loss.backward()` to compute unbiased gradients on a single batch; validation/test loaders throw an error if `shuffle=True` is passed.",
            "D": "`shuffle=True` balances minority and majority classes into equal 50/50 ratios in every batch."
        },
        "correct": ["A"],
        "explanation": (
            "Reshuffling training data at every epoch (`shuffle=True`) breaks correlations between consecutive samples "
            "(such as datasets sorted by class or time), preventing the optimizer from memorizing sample order and reducing "
            "overfitting. For validation and test sets, weights are not updated and average metrics over the entire split "
            "are order-invariant, so `shuffle=False` is standard to keep evaluation order deterministic."
        ),
        "option_explanations": {
            "A": "Correct. Shuffling training batches each epoch prevents order memorization and reduces overfitting, while `shuffle=False` keeps evaluation deterministic.",
            "B": "Incorrect. Random disk seeks are slower than sequential reads, and mean evaluation loss across the full test set is unaffected by sample order.",
            "C": "Incorrect. `loss.backward()` works regardless of `shuffle`, and PyTorch does not raise an error if `shuffle=True` is passed to a test loader.",
            "D": "Incorrect. `shuffle=True` performs a uniform random permutation (`RandomSampler`) and does not alter class proportions (which requires `WeightedRandomSampler`)."
        },
        "competency": "Explain the purpose of shuffle=True during training vs shuffle=False during evaluation",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb"
    },
    {
        "id": "PTCA-D-028",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "Based on `pytorch_data_utilities.ipynb`, how does setting `pin_memory=True` in `DataLoader` improve "
            "training throughput, and when does it provide NO performance benefit?"
        ),
        "code": (
            "train_loader = DataLoader(\n"
            "    training_data, batch_size=64, shuffle=True, pin_memory=True\n"
            ")"
        ),
        "options": {
            "A": "It caches the entire dataset inside GPU L2 cache; it provides no benefit when `batch_size > 32`.",
            "B": "It allocates CPU batch tensors directly in page-locked (pinned) host memory to accelerate CPU-to-GPU DMA transfers; it provides no performance benefit when training exclusively on a CPU.",
            "C": "It locks model weights in CPU RAM so the OS swap daemon cannot page them out; it provides no benefit on Linux.",
            "D": "It automatically moves batches to `cuda:0` without calling `.to(device)`; it provides no benefit when using `nn.DataParallel`."
        },
        "correct": ["B"],
        "explanation": (
            "As explained in `pytorch_data_utilities.ipynb`: by default, the CPU loads batch data into pageable memory, "
            "which must first be copied to a temporary pinned buffer before transferring to the GPU. Setting `pin_memory=True` "
            "loads batch tensors directly into page-locked (pinned) host memory, enabling faster CPU-to-GPU transfer. "
            "When training on a CPU only, no CPU-to-GPU copy occurs, so `pin_memory=True` gives no performance benefit."
        ),
        "option_explanations": {
            "A": "Incorrect. Pinned memory is page-locked *host (CPU)* RAM, not GPU L2 cache.",
            "B": "Correct. `pin_memory=True` places batches in page-locked host memory for faster host-to-device transfers and offers no speedup for CPU-only training.",
            "C": "Incorrect. `pin_memory=True` applies to batch tensors produced by the `DataLoader`, not model parameters.",
            "D": "Incorrect. `pin_memory=True` returns CPU tensors in pinned host memory; you still must call `.to(device)` to move them to the GPU."
        },
        "competency": "Explain the mechanism and hardware requirements of DataLoader pin_memory=True",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb"
    },
    {
        "id": "PTCA-D-029",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "When `pin_memory=True` is enabled on a `DataLoader`, which argument should be passed to `.to(device, ...)` "
            "inside the GPU training loop so that the host-to-device memory transfer can overlap asynchronously with "
            "CPU execution?"
        ),
        "code": (
            "train_loader = DataLoader(train_ds, batch_size=64, shuffle=True, num_workers=4, pin_memory=True)\n\n"
            "for x, y in train_loader:\n"
            "    x = x.to(device, ???)\n"
            "    y = y.to(device, ???)"
        ),
        "options": {
            "A": "`async_copy=True`",
            "B": "`non_blocking=True`",
            "C": "`pin_memory=True`",
            "D": "`inplace=True`"
        },
        "correct": ["B"],
        "explanation": (
            "When a CPU tensor resides in pinned (page-locked) memory (`tensor.is_pinned() == True`), calling "
            "`tensor.to(device, non_blocking=True)` initiates an asynchronous CUDA DMA transfer (`cudaMemcpyAsync`) "
            "without blocking the host CPU thread."
        ),
        "option_explanations": {
            "A": "Incorrect. `Tensor.to()` does not have an `async_copy` argument.",
            "B": "Correct. `non_blocking=True` enables asynchronous host-to-device transfers when the source tensor is in pinned memory.",
            "C": "Incorrect. `pin_memory` is a `DataLoader` argument or `Tensor.pin_memory()` method, not a keyword argument to `.to()`.",
            "D": "Incorrect. `Tensor.to()` does not accept `inplace=True`."
        },
        "competency": "Combine DataLoader pin_memory=True with Tensor.to(device, non_blocking=True)",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-030",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "What happens when you instantiate the `DataLoader` below with both a custom `sampler` and `shuffle=True`?"
        ),
        "code": (
            "from torch.utils.data import DataLoader, RandomSampler\n\n"
            "sampler = RandomSampler(train_ds)\n"
            "loader = DataLoader(train_ds, batch_size=32, sampler=sampler, shuffle=True)"
        ),
        "options": {
            "A": "The `DataLoader` applies `sampler` first and then shuffles the resulting indices a second time.",
            "B": "`shuffle=True` overrides `sampler` and logs a `UserWarning`.",
            "C": "`DataLoader` raises a `ValueError: sampler option is mutually exclusive with shuffle`.",
            "D": "It shuffles the samples inside each batch of 32 after `sampler` selects the batch."
        },
        "correct": ["C"],
        "explanation": (
            "In `DataLoader`, the `shuffle` flag simply tells `DataLoader` whether to construct a default `RandomSampler` "
            "(`shuffle=True`) or `SequentialSampler` (`shuffle=False`). If you explicitly provide a `sampler` (or "
            "`batch_sampler`), `shuffle` cannot be `True`; otherwise `DataLoader.__init__` raises "
            "`ValueError: sampler option is mutually exclusive with shuffle`."
        ),
        "option_explanations": {
            "A": "Incorrect. `DataLoader` does not chain multiple samplers.",
            "B": "Incorrect. `DataLoader` raises a hard `ValueError` rather than issuing a warning.",
            "C": "Correct. Passing both `sampler=...` and `shuffle=True` raises a `ValueError` due to mutual exclusivity.",
            "D": "Incorrect. Construction fails immediately with a `ValueError`."
        },
        "competency": "Configure custom Samplers in DataLoader and respect mutual exclusivity with shuffle",
        "source": "LFD2001 Ch. 3"
    },
]

QUESTIONS.extend([
    {
        "id": "PTCA-D-031",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Hard",
        "multi_select": False,
        "stem": (
            "You have a binary classification dataset of $N = 1,000$ samples where class `0` has $900$ samples and "
            "class `1` has $100$ samples. You want `WeightedRandomSampler` to draw balanced minibatches (approx. 50% class `0` "
            "and 50% class `1`). How must the `weights` argument passed to `WeightedRandomSampler(weights, num_samples=1000, replacement=True)` "
            "be constructed?"
        ),
        "code": (
            "import torch\n"
            "from torch.utils.data import WeightedRandomSampler\n\n"
            "# labels is a 1D tensor of length 1000 containing 900 zeros and 100 ones\n"
            "class_counts = torch.bincount(labels)          # tensor([900, 100])\n"
            "class_weights = 1.0 / class_counts.float()     # tensor([1/900, 1/100])"
        ),
        "options": {
            "A": "Pass `class_weights` of length 2 (`[1/900, 1/100]`) directly as `weights`.",
            "B": "Create a per-sample weight sequence `sample_weights = class_weights[labels]` of length 1,000 and pass `sample_weights` as `weights`.",
            "C": "Pass `class_counts` (`[900, 100]`) directly as `weights` with `replacement=False`.",
            "D": "Pass a 2D tensor of shape `(1000, 2)` containing one-hot encoded class weights."
        },
        "correct": ["B"],
        "explanation": (
            "A common pitfall with `WeightedRandomSampler(weights, num_samples, replacement=True)` is passing a vector "
            "of length `num_classes` (`2`) instead of length `len(dataset)` (`1000`). In `WeightedRandomSampler`, `weights[i]` "
            "is the sampling weight of the `i`-th *sample* in the dataset. If `weights` has length 2, only indices `0` and `1` "
            "of the dataset will ever be sampled! Indexing `sample_weights = class_weights[labels]` assigns `1/900` to every "
            "class-0 sample and `1/100` to every class-1 sample."
        ),
        "option_explanations": {
            "A": "Incorrect. If `weights` has length 2, `WeightedRandomSampler` only ever draws dataset indices `0` and `1`, ignoring indices `2..999`.",
            "B": "Correct. `WeightedRandomSampler` requires a weight for each sample index (`len(weights) == len(dataset)`), mapping each sample's label to its inverse class frequency.",
            "C": "Incorrect. Passing `class_counts` has length 2 and also weights the majority class 9x higher than the minority class.",
            "D": "Incorrect. `weights` must be a 1D sequence of non-negative numbers of length `len(dataset)`."
        },
        "competency": "Construct per-sample weight vectors for WeightedRandomSampler on imbalanced datasets",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-032",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "A natural language dataset returns variable-length token ID tensors `(seq_tensor, label)` from `__getitem__`, "
            "where `seq_tensor` has shape `(L_i,)` and $L_i$ varies between 5 and 40 across samples. When iterating over "
            "`DataLoader(nlp_ds, batch_size=8)` with the default `collate_fn`, what happens?"
        ),
        "code": (
            "class VariableLengthTextDataset(Dataset):\n"
            "    def __init__(self, sequences, labels):\n"
            "        self.sequences = sequences  # list of 1D LongTensors of varying lengths\n"
            "        self.labels = labels\n"
            "    def __len__(self):\n"
            "        return len(self.sequences)\n"
            "    def __getitem__(self, idx):\n"
            "        return self.sequences[idx], self.labels[idx]\n\n"
            "loader = DataLoader(VariableLengthTextDataset(seqs, labels), batch_size=8)\n"
            "batch = next(iter(loader))"
        ),
        "options": {
            "A": "`default_collate` automatically zero-pads all sequences in the batch to the maximum length in that batch.",
            "B": "`default_collate` truncates all sequences in the batch to the minimum length in that batch.",
            "C": "`default_collate` raises a `RuntimeError` (`stack expects each tensor to be equal size`) because `torch.stack` cannot stack tensors of different lengths.",
            "D": "`default_collate` returns a Python list of 8 unstacked 1D tensors."
        },
        "correct": ["C"],
        "explanation": (
            "As noted in `pytorch_data_utilities.ipynb`, `default_collate` attempts to combine sample tensors using "
            "`torch.stack`, which requires every tensor in the batch to have the exact same shape. Variable-length "
            "tensors trigger a `RuntimeError` unless a custom `collate_fn` (for example using `torch.nn.utils.rnn.pad_sequence`) "
            "is passed to `DataLoader`."
        ),
        "option_explanations": {
            "A": "Incorrect. Zero-padding requires a custom `collate_fn` using `nn.utils.rnn.pad_sequence`; `default_collate` does not pad.",
            "B": "Incorrect. `default_collate` never truncates tensors.",
            "C": "Correct. `default_collate` calls `torch.stack` on the sample tensors, which fails with a `RuntimeError` when sequence lengths differ.",
            "D": "Incorrect. Returning a list of variable-length tensors requires a custom `collate_fn`."
        },
        "competency": "Explain why variable-length tensors fail in default_collate and require a custom collate_fn",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb"
    },
    {
        "id": "PTCA-D-033",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "Examine the custom `collate_fn` below used to batch variable-length 1D token tensors with `pad_sequence`. "
            "If a batch of 4 samples has sequence lengths `[6, 11, 4, 9]`, what are the shapes of `padded_seqs` and `labels` "
            "returned by `pad_collate`?"
        ),
        "code": (
            "import torch\n"
            "from torch.nn.utils.rnn import pad_sequence\n\n"
            "def pad_collate(batch):\n"
            "    # batch is a list of (seq_tensor, label_int) tuples\n"
            "    seqs, labels = zip(*batch)\n"
            "    padded_seqs = pad_sequence(seqs, batch_first=True, padding_value=0)\n"
            "    return padded_seqs, torch.tensor(labels, dtype=torch.long)"
        ),
        "options": {
            "A": "`padded_seqs`: `torch.Size([11, 4])`, `labels`: `torch.Size([4])`",
            "B": "`padded_seqs`: `torch.Size([4, 11])`, `labels`: `torch.Size([4])`",
            "C": "`padded_seqs`: `torch.Size([4, 30])`, `labels`: `torch.Size([4, 1])`",
            "D": "`padded_seqs`: `torch.Size([4, 4])`, `labels`: `torch.Size([4])`"
        },
        "correct": ["B"],
        "explanation": (
            "`pad_sequence(seqs, batch_first=True, padding_value=0)` pads all 1D tensors in `seqs` to the maximum length "
            "in the batch ($\\max(6, 11, 4, 9) = 11$) and places the batch dimension (`4`) first because `batch_first=True`, "
            "producing shape `(4, 11)`. `torch.tensor(labels, dtype=torch.long)` creates a 1D tensor of shape `(4,)`."
        ),
        "option_explanations": {
            "A": "Incorrect. `(11, 4)` would be the shape if `batch_first=False` (the default of `pad_sequence`), but `batch_first=True` is specified.",
            "B": "Correct. With `batch_first=True`, `pad_sequence` outputs `(batch_size, max_seq_len) = (4, 11)`, and `labels` has shape `(4,)`.",
            "C": "Incorrect. `pad_sequence` pads to the maximum length (`11`), not the sum of lengths (`30`).",
            "D": "Incorrect. `pad_sequence` pads to the longest sequence (`11`), rather than truncating to the shortest (`4`)."
        },
        "competency": "Implement a custom collate_fn with pad_sequence for variable-length sequences",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb & LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-034",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "What is the exact input argument passed to a custom `collate_fn(batch)` by `DataLoader` when `batch_size=4` "
            "and `Dataset.__getitem__` returns `(image_tensor, label_int)`?"
        ),
        "code": (
            "def my_collate_fn(batch):\n"
            "    print(type(batch), len(batch), type(batch[0]))\n"
            "    ..."
        ),
        "options": {
            "A": "A tuple of two lists: `([img0, img1, img2, img3], [lbl0, lbl1, lbl2, lbl3])`.",
            "B": "A list of 4 tuples: `[(img0, lbl0), (img1, lbl1), (img2, lbl2), (img3, lbl3)]`.",
            "C": "A dictionary `{0: (img0, lbl0), 1: (img1, lbl1), 2: (img2, lbl2), 3: (img3, lbl3)}`.",
            "D": "A generator yielding integer indices `[idx0, idx1, idx2, idx3]` before `__getitem__` is called."
        },
        "correct": ["B"],
        "explanation": (
            "For a map-style dataset with batched loading, `DataLoader` fetches `[dataset[i] for i in batch_indices]` "
            "and passes that `list` of raw sample objects to `collate_fn(batch)`. Since each `dataset[i]` is a `(img, lbl)` "
            "tuple, `batch` is a `list` of 4 `(img, lbl)` tuples."
        ),
        "option_explanations": {
            "A": "Incorrect. `batch` is not pre-transposed; transposing it is typically done inside `collate_fn` via `zip(*batch)`.",
            "B": "Correct. `collate_fn` receives the list of samples returned by `[dataset[idx] for idx in batch_indices]`.",
            "C": "Incorrect. `batch` is a `list`, not a `dict`.",
            "D": "Incorrect. `__getitem__` is already called for each index in the batch before `collate_fn` is invoked."
        },
        "competency": "Trace the input data structure received by a DataLoader collate_fn",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb & LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-035",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "In `torch.utils.data.DataLoader`, what is the difference between setting `num_workers=0` and `num_workers=4`?"
        ),
        "code": (
            "loader_a = DataLoader(train_ds, batch_size=64, num_workers=0)\n"
            "loader_b = DataLoader(train_ds, batch_size=64, num_workers=4)"
        ),
        "options": {
            "A": "`num_workers=0` disables data loading and returns empty batches, whereas `num_workers=4` loads 4 samples per batch.",
            "B": "`num_workers=0` loads and preprocesses data synchronously in the main Python process, whereas `num_workers=4` spawns 4 background subprocesses to prefetch and collate batches in parallel.",
            "C": "`num_workers=0` runs on the CPU, whereas `num_workers=4` distributes the model across 4 GPUs.",
            "D": "`num_workers=0` uses 0 threads on the GPU, whereas `num_workers=4` uses 4 CUDA streams."
        },
        "correct": ["B"],
        "explanation": (
            "In PyTorch's `DataLoader`, `num_workers=0` (the default) means data loading (`__getitem__` and `collate_fn`) "
            "executes synchronously inside the main process whenever `next(iter(loader))` is called. Setting `num_workers=k` "
            "($k > 0$) spawns $k$ worker subprocesses that load, transform, and collate batches asynchronously in the background."
        ),
        "option_explanations": {
            "A": "Incorrect. `num_workers=0` is the default setting and loads batches in the main process.",
            "B": "Correct. `num_workers=0` runs in the main process; `num_workers=4` uses 4 worker subprocesses for parallel data prefetching.",
            "C": "Incorrect. `num_workers` controls CPU data-loading subprocesses, not multi-GPU model parallelism.",
            "D": "Incorrect. `num_workers` creates OS subprocesses on the host CPU, not CUDA streams."
        },
        "competency": "Contrast main-process data loading (num_workers=0) with multi-process prefetching (num_workers > 0)",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-036",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Hard",
        "multi_select": False,
        "stem": (
            "Examine the `IterableDataset` below that yields integers `0` through `9`. If you wrap it in "
            "`loader = DataLoader(MyRangeStream(10), batch_size=5, num_workers=2)` without checking `get_worker_info()`, "
            "how many total items are yielded across one full pass over `loader`?"
        ),
        "code": (
            "import torch\n"
            "from torch.utils.data import IterableDataset, DataLoader\n\n"
            "class MyRangeStream(IterableDataset):\n"
            "    def __init__(self, n):\n"
            "        self.n = n\n"
            "    def __iter__(self):\n"
            "        return iter(range(self.n))\n\n"
            "loader = DataLoader(MyRangeStream(10), batch_size=5, num_workers=2)\n"
            "all_batches = list(loader)"
        ),
        "options": {
            "A": "10 items total (2 batches of 5), because `DataLoader` automatically shards `range(self.n)` across the 2 workers.",
            "B": "20 items total (4 batches of 5), because each of the 2 worker processes independently iterates through a full copy of `MyRangeStream(10)`.",
            "C": "5 items total (1 batch of 5), because `num_workers=2` halves the stream length.",
            "D": "A `RuntimeError` is raised because `IterableDataset` does not support `num_workers > 0`."
        },
        "correct": ["B"],
        "explanation": (
            "With an `IterableDataset` and `num_workers > 0`, each worker process gets its own shallow copy of the "
            "`dataset` object and calls `__iter__()` independently. Unless the dataset partitions the workload per worker "
            "using `torch.utils.data.get_worker_info()`, every worker yields the entire stream, resulting in "
            "$2 \\times 10 = 20$ duplicated items (4 batches of 5)."
        ),
        "option_explanations": {
            "A": "Incorrect. Unlike map-style datasets where the sampler lives in the main process, `DataLoader` cannot automatically shard an arbitrary `__iter__` stream across workers.",
            "B": "Correct. Without manual sharding via `get_worker_info()`, each of the 2 workers yields all 10 items, producing 20 items (4 batches of 5).",
            "C": "Incorrect. Workers duplicate the unsharded stream rather than halving it.",
            "D": "Incorrect. `IterableDataset` supports `num_workers > 0`, but requires explicit worker partitioning to avoid duplicate data."
        },
        "competency": "Prevent duplicate data across workers in IterableDataset using torch.utils.data.get_worker_info()",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-037",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Hard",
        "multi_select": False,
        "stem": (
            "How should `__iter__` in an `IterableDataset` use `torch.utils.data.get_worker_info()` so that it works "
            "correctly both when `num_workers=0` (single-process) and when `num_workers > 0` (multi-process)?"
        ),
        "code": (
            "import math\n"
            "import torch\n"
            "from torch.utils.data import IterableDataset, get_worker_info\n\n"
            "class ShardedStream(IterableDataset):\n"
            "    def __init__(self, start, end):\n"
            "        self.start = start\n"
            "        self.end = end\n"
            "    def __iter__(self):\n"
            "        worker_info = get_worker_info()\n"
            "        # How should worker_info be handled?"
        ),
        "options": {
            "A": "When `num_workers=0`, `get_worker_info()` returns `None` (yield full range `start..end`); when `num_workers > 0`, use `worker_info.id` and `worker_info.num_workers` to compute a disjoint sub-range for that worker.",
            "B": "`get_worker_info()` always returns an object with `id=0, num_workers=1` when `num_workers=0`, so checking for `None` is an error.",
            "C": "Call `worker_info.shard(self.start, self.end)` which is a built-in method on `WorkerInfo`.",
            "D": "Call `get_worker_info()` inside `__init__` so the dataset is partitioned before `DataLoader` is constructed."
        },
        "correct": ["A"],
        "explanation": (
            "`torch.utils.data.get_worker_info()` returns `None` when called in the main process (`num_workers=0`), and "
            "returns a `WorkerInfo(id, num_workers, seed, dataset)` instance when called inside a `DataLoader` worker "
            "process (`num_workers > 0`). Checking `if worker_info is None:` handles single-process loading, while the "
            "`else` branch uses `worker_info.id` and `worker_info.num_workers` inside `__iter__` (or `worker_init_fn`) "
            "to assign each worker a unique shard."
        ),
        "option_explanations": {
            "A": "Correct. `get_worker_info()` returns `None` in the main process and a `WorkerInfo` object with `.id` and `.num_workers` in worker processes.",
            "B": "Incorrect. In the main process (`num_workers=0`), `get_worker_info()` returns `None`, so accessing `.id` without a `None` check raises `AttributeError`.",
            "C": "Incorrect. `WorkerInfo` only exposes attributes (`id`, `num_workers`, `seed`, `dataset`) and has no `.shard()` method.",
            "D": "Incorrect. `__init__` runs in the main process before workers exist, where `get_worker_info()` is always `None`."
        },
        "competency": "Partition IterableDataset streams across DataLoader workers with get_worker_info()",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-038",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "What is the effect of setting `persistent_workers=True` in `DataLoader(train_ds, batch_size=64, num_workers=4, persistent_workers=True)`?"
        ),
        "code": (
            "train_loader = DataLoader(\n"
            "    train_ds,\n"
            "    batch_size=64,\n"
            "    shuffle=True,\n"
            "    num_workers=4,\n"
            "    persistent_workers=True\n"
            ")"
        ),
        "options": {
            "A": "It saves worker process states to disk so training can resume after a system reboot.",
            "B": "It keeps the 4 worker subprocesses alive across epochs instead of shutting them down at the end of each epoch and respawning them at the start of the next epoch.",
            "C": "It allows `persistent_workers=True` to be used with `num_workers=0` to cache batches on the GPU.",
            "D": "It prevents `shuffle=True` from generating a new permutation on subsequent epochs."
        },
        "correct": ["B"],
        "explanation": (
            "By default (`persistent_workers=False`), `DataLoader` terminates all worker processes when an epoch finishes "
            "and spawns new worker processes at the start of the next epoch. Setting `persistent_workers=True` (valid "
            "only when `num_workers > 0`) keeps the worker processes alive across epochs, eliminating process creation "
            "overhead and preserving worker-local state between epochs."
        ),
        "option_explanations": {
            "A": "Incorrect. `persistent_workers=True` does not checkpoint processes to disk.",
            "B": "Correct. Worker processes remain alive between epochs rather than being torn down and recreated every epoch.",
            "C": "Incorrect. Setting `persistent_workers=True` when `num_workers=0` raises a `ValueError: persistent_workers option needs num_workers > 0`.",
            "D": "Incorrect. `shuffle=True` still generates a fresh random permutation in the main process each epoch and sends new index batches to the persistent workers."
        },
        "competency": "Optimize multi-epoch DataLoader startup overhead using persistent_workers=True",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-039",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "A developer wants to move sample tensors to the GPU inside `Dataset.__getitem__` as shown below, and then "
            "passes the dataset to `DataLoader(ds, batch_size=32, num_workers=4)` on Linux (default `'fork'` start method). "
            "What happens when iterating over the `DataLoader`?"
        ),
        "code": (
            "class GpuInsideDataset(Dataset):\n"
            "    def __init__(self, data):\n"
            "        self.data = data\n"
            "    def __len__(self):\n"
            "        return len(self.data)\n"
            "    def __getitem__(self, idx):\n"
            "        # Attempt to move sample directly to CUDA inside worker:\n"
            "        return self.data[idx].to('cuda')\n\n"
            "loader = DataLoader(GpuInsideDataset(torch.randn(100, 10)), batch_size=32, num_workers=4)"
        ),
        "options": {
            "A": "It achieves 4x faster GPU utilization than moving batches in the training loop.",
            "B": "If CUDA was initialized in the main process, forked worker processes fail with `RuntimeError: Cannot re-initialize CUDA in forked subprocess`; best practice is to return CPU tensors from `__getitem__`, use `pin_memory=True`, and call `.to('cuda')` on the collated batch in the main process.",
            "C": "It works without issue because `fork` shares the CUDA context across all child processes.",
            "D": "`DataLoader` automatically rewrites `.to('cuda')` into `.to('cpu')` inside worker subprocesses."
        },
        "correct": ["B"],
        "explanation": (
            "CUDA contexts cannot be re-initialized inside `fork`-ed child processes (`RuntimeError: Cannot re-initialize "
            "CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method`). Moreover, "
            "doing small per-sample host-to-GPU transfers in workers is inefficient compared to returning CPU tensors, "
            "collating them into a pinned-memory batch (`pin_memory=True`), and transferring the entire batch once via "
            "`batch.to(device, non_blocking=True)` in the main training loop."
        ),
        "option_explanations": {
            "A": "Incorrect. Initializing CUDA in forked workers crashes, and per-sample GPU transfers are much slower than batched DMA transfers.",
            "B": "Correct. Forked workers cannot re-initialize CUDA; `Dataset.__getitem__` should return CPU tensors and let the main loop move collated batches to the GPU.",
            "C": "Incorrect. The CUDA runtime explicitly forbids re-initializing CUDA after an OS `fork()`.",
            "D": "Incorrect. `DataLoader` does not intercept or rewrite `.to('cuda')` calls inside `__getitem__`."
        },
        "competency": "Avoid CUDA initialization errors in forked DataLoader workers by keeping Dataset outputs on CPU",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-040",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "In `DataLoader`, what happens when you explicitly set `batch_size=None` (and `batch_sampler=None`) on a "
            "map-style dataset whose `__getitem__(self, idx)` returns a tensor of shape `(3, 64, 64)`?"
        ),
        "code": (
            "loader = DataLoader(image_dataset, batch_size=None)\n"
            "item = next(iter(loader))"
        ),
        "options": {
            "A": "`DataLoader` raises a `ValueError` because `batch_size` must be a positive integer.",
            "B": "`DataLoader` disables automatic batching (`_auto_collation`), so each iteration returns the individual sample directly with shape `(3, 64, 64)` instead of `(1, 3, 64, 64)`.",
            "C": "`DataLoader` loads the entire dataset as a single giant batch of shape `(N, 3, 64, 64)`.",
            "D": "`batch_size=None` is identical to `batch_size=1` and returns shape `(1, 3, 64, 64)`."
        },
        "correct": ["B"],
        "explanation": (
            "Setting `batch_size=None` (with `batch_sampler=None`) disables automatic batching in `DataLoader`. Instead "
            "of wrapping indices in a `BatchSampler` and stacking a list of samples with `default_collate`, `DataLoader` "
            "yields individual dataset items directly as returned by `__getitem__` (useful when the dataset itself "
            "already returns pre-batched tensors)."
        ),
        "option_explanations": {
            "A": "Incorrect. `batch_size=None` is explicitly supported in `DataLoader` to disable automatic batching.",
            "B": "Correct. With `batch_size=None`, automatic batching is disabled and `item` has the unbatched shape `(3, 64, 64)`.",
            "C": "Incorrect. Loading the full dataset as one batch requires `batch_size=len(image_dataset)`.",
            "D": "Incorrect. `batch_size=1` adds a leading batch dimension `(1, 3, 64, 64)`, whereas `batch_size=None` omits the batch dimension."
        },
        "competency": "Understand automatic vs disabled batching when batch_size=None in DataLoader",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-041",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": True,
        "stem": (
            "You pass a custom `batch_sampler` (an instance of `torch.utils.data.BatchSampler` yielding lists of indices) "
            "to `DataLoader(dataset, batch_sampler=my_batch_sampler)`. Which TWO of the following statements are true "
            "about the remaining `DataLoader` arguments?"
        ),
        "code": (
            "from torch.utils.data import DataLoader, BatchSampler, SequentialSampler\n\n"
            "my_batch_sampler = BatchSampler(SequentialSampler(ds), batch_size=16, drop_last=True)\n"
            "loader = DataLoader(ds, batch_sampler=my_batch_sampler)"
        ),
        "options": {
            "A": "`batch_sampler` is mutually exclusive with `batch_size`, `shuffle`, `sampler`, and `drop_last` (passing non-default values for any of those four raises a `ValueError`).",
            "B": "You must also pass `batch_size=16` and `drop_last=True` to `DataLoader` so they match `my_batch_sampler`.",
            "C": "You can still specify `num_workers`, `pin_memory`, and `collate_fn` alongside `batch_sampler`.",
            "D": "`batch_sampler` can only be used with `IterableDataset` subclasses."
        },
        "correct": ["A", "C"],
        "explanation": (
            "When `batch_sampler` is provided to `DataLoader`, it already encapsulates index sampling, batch size, and "
            "`drop_last` behavior. Therefore, `DataLoader` enforces that `batch_size=1`, `shuffle=False`, `sampler=None`, "
            "and `drop_last=False` remain at their defaults; setting any of them raises a `ValueError: batch_sampler option "
            "is mutually exclusive with batch_size, shuffle, sampler, and drop_last`. Worker, memory, and collation options "
            "(`num_workers`, `pin_memory`, `collate_fn`) remain fully configurable."
        ),
        "option_explanations": {
            "A": "Correct. `batch_sampler` is mutually exclusive with `batch_size`, `shuffle`, `sampler`, and `drop_last`.",
            "B": "Incorrect. Passing `batch_size=16` or `drop_last=True` alongside `batch_sampler` raises a `ValueError`.",
            "C": "Correct. `num_workers`, `pin_memory`, and `collate_fn` are independent of `batch_sampler` and work normally.",
            "D": "Incorrect. `batch_sampler` is for map-style datasets and is mutually exclusive with `IterableDataset`."
        },
        "competency": "Configure custom BatchSampler instances in DataLoader and recognize mutually exclusive arguments",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-042",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "In `pytorch_data_utilities.ipynb`, the `FashionMNIST` training `DataLoader` is configured with `batch_size=64` "
            "and `ToTensor()`. When the code below executes, what is printed for `train_features.size()` and `train_labels.size()`?"
        ),
        "code": (
            "train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)\n"
            "train_features, train_labels = next(iter(train_dataloader))\n"
            "print(f'Feature batch shape: {train_features.size()}')\n"
            "print(f'Labels batch shape: {train_labels.size()}')"
        ),
        "options": {
            "A": "`Feature batch shape: torch.Size([64, 28, 28, 1])` and `Labels batch shape: torch.Size([64, 1])`",
            "B": "`Feature batch shape: torch.Size([64, 1, 28, 28])` and `Labels batch shape: torch.Size([64])`",
            "C": "`Feature batch shape: torch.Size([1, 64, 28, 28])` and `Labels batch shape: torch.Size([1, 64])`",
            "D": "`Feature batch shape: torch.Size([64, 784])` and `Labels batch shape: torch.Size([64, 10])`"
        },
        "correct": ["B"],
        "explanation": (
            "Each `FashionMNIST` sample has image tensor shape `(1, 28, 28)` and an integer scalar label. Collating 64 "
            "samples stacks them along a new leading batch dimension (`dim=0`), yielding `torch.Size([64, 1, 28, 28])` "
            "for `train_features` and `torch.Size([64])` for `train_labels`, matching Cell 4 of `pytorch_data_utilities.ipynb`."
        ),
        "option_explanations": {
            "A": "Incorrect. PyTorch uses channel-first `(N, C, H, W)` layout, and integer labels collate to 1D `(64,)`, not `(64, 1)`.",
            "B": "Correct. This matches the exact output in `pytorch_data_utilities.ipynb`: `[64, 1, 28, 28]` and `[64]`.",
            "C": "Incorrect. The batch dimension `64` is always placed at dimension 0 by `default_collate`.",
            "D": "Incorrect. `ToTensor()` does not flatten images to `784` or one-hot encode labels to `10`."
        },
        "competency": "Predict batched feature and label tensor shapes emitted by a DataLoader",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb"
    },
    {
        "id": "PTCA-D-043",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "You are evaluating a regression model on a test set of $N = 1,010$ samples using "
            "`test_loader = DataLoader(test_ds, batch_size=100, shuffle=False, drop_last=False)` and "
            "`criterion = nn.MSELoss(reduction='mean')`. Why does computing the test MSE as "
            "`sum(criterion(model(x), y).item() for x, y in test_loader) / len(test_loader)` produce a slightly "
            "incorrect dataset-wide mean squared error?"
        ),
        "code": (
            "# len(test_ds) == 1010, batch_size == 100 -> 10 batches of 100 and 1 batch of 10\n"
            "criterion = torch.nn.MSELoss(reduction='mean')\n\n"
            "batch_losses = []\n"
            "with torch.no_grad():\n"
            "    for x, y in test_loader:\n"
            "        batch_losses.append(criterion(model(x), y).item())\n"
            "naive_test_mse = sum(batch_losses) / len(test_loader)"
        ),
        "options": {
            "A": "Because `MSELoss(reduction='mean')` divides by `batch_size=100` even on the 11th batch that only has 10 samples.",
            "B": "Because the 11th batch has only 10 samples ($1010 \\pmod{100} = 10$), yet averaging the 11 batch means gives the 10-sample final batch the same $1/11$ weight as each 100-sample batch instead of weighting each batch loss by `x.size(0)` (or using `reduction='sum'` and dividing by `len(test_ds)`).",
            "C": "Because `shuffle=False` biases `MSELoss` toward the last batch.",
            "D": "Because `len(test_loader)` returns `1010` instead of `11`."
        },
        "correct": ["B"],
        "explanation": (
            "When $N$ is not divisible by `batch_size` and `drop_last=False`, the final batch is smaller ($10$ samples "
            "vs $100$). Taking an unweighted average of the 11 batch means over-weights each sample in the 10-sample "
            "batch by a factor of $10\\times$. To compute the exact dataset mean loss, either accumulate "
            "`criterion(pred, y).item() * x.size(0)` and divide by `len(test_ds)`, or use `reduction='sum'` and divide "
            "by `len(test_ds)` (as done in `pytorch_nn_linear.ipynb`)."
        ),
        "option_explanations": {
            "A": "Incorrect. `MSELoss(reduction='mean')` divides by the actual number of elements in the input tensor (`10` on the last batch).",
            "B": "Correct. Unweighted averaging of batch means gives equal weight to unequal-sized batches; weighting by `x.size(0)` or summing and dividing by `len(test_ds)` gives the true dataset mean.",
            "C": "Incorrect. The sum of squared errors across all samples is commutative and unaffected by `shuffle`.",
            "D": "Incorrect. `len(test_loader)` returns the number of batches (`11`), whereas `len(test_loader.dataset)` returns `1010`."
        },
        "competency": "Accurately aggregate evaluation loss across DataLoader batches when the final batch is smaller",
        "source": "modules/module_6_pytorch_nn_hands_on/pytorch_nn_linear.ipynb & LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-044",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "On Windows or macOS (where Python's `multiprocessing` defaults to the `'spawn'` start method), a script "
            "defines a `DataLoader` with `num_workers=4` and runs the training loop at the top level of `train.py` "
            "WITHOUT an `if __name__ == '__main__':` guard. What happens when `python train.py` is executed?"
        ),
        "code": (
            "# train.py (no if __name__ == '__main__': guard)\n"
            "import torch\n"
            "from torch.utils.data import TensorDataset, DataLoader\n\n"
            "ds = TensorDataset(torch.randn(100, 4), torch.zeros(100))\n"
            "loader = DataLoader(ds, batch_size=16, num_workers=4)\n"
            "for x, y in loader:\n"
            "    pass"
        ),
        "options": {
            "A": "PyTorch silently falls back to `num_workers=0` and prints nothing.",
            "B": "Each spawned worker imports `train.py` from the top, attempting to spawn new workers recursively, and Python's `multiprocessing` raises a `RuntimeError` regarding starting a new process before the current process has finished bootstrapping.",
            "C": "The script runs 4 complete training loops in parallel and finishes 4x faster.",
            "D": "`TensorDataset` raises a `PicklingError` because tensors cannot be serialized with `spawn`."
        },
        "correct": ["B"],
        "explanation": (
            "Under the `'spawn'` start method (default on Windows and macOS), each worker process starts a fresh Python "
            "interpreter and re-imports the main script (`train.py`) to reconstruct objects. If `for x, y in loader:` is "
            "not protected inside `if __name__ == '__main__':`, the child process executes the loop during import and "
            "tries to spawn its own workers, triggering Python's `RuntimeError: An attempt has been made to start a new "
            "process before the current process has finished its bootstrapping phase`."
        ),
        "option_explanations": {
            "A": "Incorrect. PyTorch does not silently downgrade `num_workers` to 0.",
            "B": "Correct. With `'spawn'`, top-level iteration over a multi-worker `DataLoader` without `if __name__ == '__main__':` causes recursive process spawning and raises a `RuntimeError`.",
            "C": "Incorrect. The recursive spawn attempt is blocked by Python's multiprocessing bootstrap check.",
            "D": "Incorrect. `TensorDataset` and `torch.Tensor` are fully picklable across spawned processes."
        },
        "competency": "Handle multiprocessing spawn requirements when using DataLoader with num_workers > 0",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-045",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "What does `torch.utils.data.SubsetRandomSampler(indices)` do when passed to `DataLoader(dataset, batch_size=32, sampler=SubsetRandomSampler(train_indices))`?"
        ),
        "code": (
            "from torch.utils.data import DataLoader, SubsetRandomSampler\n\n"
            "train_indices = [0, 2, 5, 8, 11, 14, 19, 22]\n"
            "loader = DataLoader(full_dataset, batch_size=4, sampler=SubsetRandomSampler(train_indices))"
        ),
        "options": {
            "A": "It samples indices randomly from `0` to `len(full_dataset) - 1` excluding `train_indices`.",
            "B": "It randomly shuffles and yields elements ONLY from the provided list `train_indices` without replacement on each epoch.",
            "C": "It samples from `train_indices` in strict sequential order `[0, 2, 5, 8, ...]`.",
            "D": "It creates a deep copy of `full_dataset` containing only the samples at `train_indices`."
        },
        "correct": ["B"],
        "explanation": (
            "`SubsetRandomSampler(indices)` samples elements randomly from a given list of `indices`, without replacement "
            "(`for i in torch.randperm(len(self.indices)): yield self.indices[i]`). Note that because `sampler` is passed, "
            "`shuffle` must remain `False` (default) on the `DataLoader`."
        ),
        "option_explanations": {
            "A": "Incorrect. `SubsetRandomSampler` draws *from* `indices`, not the complement of `indices`.",
            "B": "Correct. `SubsetRandomSampler` yields a random permutation of the specified `indices` without replacement every epoch.",
            "C": "Incorrect. It permutes `indices` randomly via `torch.randperm`, rather than yielding them sequentially.",
            "D": "Incorrect. A `Sampler` only yields integer indices and never copies or holds the dataset itself."
        },
        "competency": "Use SubsetRandomSampler to sample randomly from index splits",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-046",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "You want `RandomSampler` to draw *with replacement* and generate exactly $5,000$ samples per epoch from a "
            "small dataset of $N = 800$ samples. How do you configure `RandomSampler`?"
        ),
        "code": (
            "from torch.utils.data import RandomSampler, DataLoader\n\n"
            "# len(small_ds) == 800\n"
            "sampler = RandomSampler(small_ds, ???)"
        ),
        "options": {
            "A": "`RandomSampler(small_ds, replacement=True, num_samples=5000)`",
            "B": "`RandomSampler(small_ds, replacement=False, num_samples=5000)`",
            "C": "`RandomSampler(small_ds, oversample_factor=6.25)`",
            "D": "`RandomSampler` does not support sampling with replacement; only `SequentialSampler` does."
        },
        "correct": ["A"],
        "explanation": (
            "`torch.utils.data.RandomSampler(data_source, replacement=False, num_samples=None)` supports drawing with "
            "replacement when `replacement=True`, allowing `num_samples` to be set to any positive integer (including "
            "values larger than `len(data_source)`, such as `5000`)."
        ),
        "option_explanations": {
            "A": "Correct. Setting `replacement=True` and `num_samples=5000` draws 5,000 indices uniformly at random with replacement per epoch.",
            "B": "Incorrect. When `replacement=False`, setting `num_samples > len(data_source)` is invalid because you cannot draw 5,000 unique items from 800 samples without replacement.",
            "C": "Incorrect. `RandomSampler` has no `oversample_factor` parameter.",
            "D": "Incorrect. `RandomSampler` supports `replacement=True`, whereas `SequentialSampler` simply yields `0..N-1` in order."
        },
        "competency": "Configure RandomSampler with replacement=True and custom num_samples",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-047",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Hard",
        "multi_select": False,
        "stem": (
            "In `DataLoader`, what does the `prefetch_factor` parameter control (default `prefetch_factor=2` when "
            "`num_workers > 0`), and what happens if you pass `prefetch_factor=4` when `num_workers=0`?"
        ),
        "code": (
            "loader = DataLoader(train_ds, batch_size=32, num_workers=0, prefetch_factor=4)"
        ),
        "options": {
            "A": "It controls how many batches are pre-copied to GPU VRAM; with `num_workers=0` it prefetches 4 batches on a CUDA stream.",
            "B": "It specifies the number of batches loaded in advance *by each worker* (`total_prefetched = prefetch_factor * num_workers`); setting `prefetch_factor` when `num_workers=0` raises a `ValueError`.",
            "C": "It specifies how many epochs are pre-computed in CPU RAM; with `num_workers=0` it is silently ignored.",
            "D": "It controls the number of individual samples (not batches) read per disk seek."
        },
        "correct": ["B"],
        "explanation": (
            "`prefetch_factor` specifies the number of batches prefetched in advance by *each* worker process (so with "
            "`num_workers=4` and default `prefetch_factor=2`, up to $4 \\times 2 = 8$ batches are queued). Because main-process "
            "loading (`num_workers=0`) does not prefetch in background workers, passing a non-`None` `prefetch_factor` "
            "when `num_workers=0` raises `ValueError: prefetch_factor option could only be specified in multiprocessing. "
            "let num_workers > 0 to enable multiprocessing`."
        ),
        "option_explanations": {
            "A": "Incorrect. `prefetch_factor` queues batches in host memory via CPU workers, not GPU VRAM, and fails when `num_workers=0`.",
            "B": "Correct. `prefetch_factor` sets the number of batches prefetched per worker and raises a `ValueError` if specified when `num_workers=0`.",
            "C": "Incorrect. It counts batches per worker, not epochs, and is not silently ignored when `num_workers=0`.",
            "D": "Incorrect. `prefetch_factor` is measured in *batches* per worker, not individual samples."
        },
        "competency": "Configure DataLoader prefetch_factor and understand its dependency on num_workers > 0",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-048",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "You create an `IterableDataset` that streams rows from a database cursor without implementing `__len__`. "
            "What happens when a training progress bar (such as `tqdm(loader)`) calls `len(loader)` on "
            "`loader = DataLoader(stream_ds, batch_size=32)`?"
        ),
        "code": (
            "class CursorStreamDataset(IterableDataset):\n"
            "    def __iter__(self):\n"
            "        for row in fetch_rows():\n"
            "            yield row\n\n"
            "loader = DataLoader(CursorStreamDataset(), batch_size=32)\n"
            "n_batches = len(loader)"
        ),
        "options": {
            "A": "`len(loader)` consumes the entire iterator to count the batches and resets the cursor.",
            "B": "`len(loader)` raises `TypeError: object of type 'CursorStreamDataset' has no len()`.",
            "C": "`len(loader)` returns `0` for any `IterableDataset`.",
            "D": "`len(loader)` returns `32` (the `batch_size`)."
        },
        "correct": ["B"],
        "explanation": (
            "`DataLoader.__len__` checks whether `self.dataset` is an `IterableDataset` and delegates to `len(self.dataset)` "
            "(dividing by `batch_size`). If the `IterableDataset` does not implement `__len__`, calling `len(loader)` "
            "raises `TypeError: object of type 'CursorStreamDataset' has no len()`."
        ),
        "option_explanations": {
            "A": "Incorrect. `len(loader)` never consumes the stream to count items.",
            "B": "Correct. Without `__len__` defined on the `IterableDataset`, `len(loader)` raises a `TypeError`.",
            "C": "Incorrect. Python's `len()` raises `TypeError` rather than returning `0` when `__len__` is undefined.",
            "D": "Incorrect. `len(loader)` represents the number of batches, not `batch_size`."
        },
        "competency": "Predict len(dataloader) behavior when wrapping an IterableDataset without __len__",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-049",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "A custom `collate_fn` uses a local `lambda` expression inside `create_loader()` as shown below. "
            "When `num_workers=2` is used on a platform with the `'spawn'` multiprocessing start method (Windows/macOS), "
            "what error occurs when iteration begins?"
        ),
        "code": (
            "def create_loader(dataset):\n"
            "    return DataLoader(\n"
            "        dataset,\n"
            "        batch_size=16,\n"
            "        num_workers=2,\n"
            "        collate_fn=lambda batch: tuple( zip(*batch) )\n"
            "    )"
        ),
        "options": {
            "A": "`AttributeError: Can't pickle local object 'create_loader.<locals>.<lambda>'` because `spawn` serializes `collate_fn` with `pickle` to send it to worker processes.",
            "B": "`SyntaxError` because `DataLoader` does not accept `lambda` functions even when `num_workers=0`.",
            "C": "`RuntimeError: zip(*batch) can only be called on GPU tensors`.",
            "D": "No error occurs because Python's standard `pickle` module can serialize any anonymous `lambda` function."
        },
        "correct": ["A"],
        "explanation": (
            "When `num_workers > 0` under the `'spawn'` start method, `DataLoader` must serialize (`pickle`) the dataset, "
            "`collate_fn`, and `worker_init_fn` to pass them to child processes. Python's standard `pickle` module cannot "
            "pickle `lambda` functions or nested local functions (`AttributeError: Can't pickle local object ...`). "
            "Defining `collate_fn` as a top-level `def` function at module scope resolves the issue."
        ),
        "option_explanations": {
            "A": "Correct. Standard `pickle` cannot serialize `lambda` or inner functions when spawning worker processes.",
            "B": "Incorrect. When `num_workers=0`, no pickling occurs and a `lambda` `collate_fn` runs fine in the main process.",
            "C": "Incorrect. `zip(*batch)` is a standard Python built-in that works on any iterable.",
            "D": "Incorrect. Standard `pickle` requires functions to be importable by module and qualified name at top-level scope, which `lambda` lacks."
        },
        "competency": "Avoid pickling errors with lambda collate_fn or worker_init_fn in multi-worker DataLoaders",
        "source": "LFD2001 Ch. 3"
    },
    {
        "id": "PTCA-D-050",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D2,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "If you set `num_workers` on a `DataLoader` to an excessively high number (e.g., `num_workers=32` on a "
            "4-core CPU machine with limited RAM), which of the following degrades performance or causes failures?"
        ),
        "code": (
            "# Running on a 4-CPU-core machine with 8 GB RAM:\n"
            "loader = DataLoader(large_image_ds, batch_size=128, num_workers=32, pin_memory=True)"
        ),
        "options": {
            "A": "PyTorch raises a `ValueError` whenever `num_workers` exceeds `os.cpu_count()`.",
            "B": "Excessive worker processes cause heavy CPU context-switching overhead, disk I/O thrashing, and high host RAM / shared-memory (`/dev/shm`) consumption from `32 * prefetch_factor` queued batches.",
            "C": "`DataLoader` automatically reduces `batch_size` to `128 // 32 = 4` per step.",
            "D": "Each worker claims an exclusive GPU, causing a `RuntimeError: invalid device ordinal`."
        },
        "correct": ["B"],
        "explanation": (
            "Each worker process holds its own copy of the dataset metadata and prefetches `prefetch_factor` full batches "
            "into shared memory (`/dev/shm` on Linux) or host RAM. Spawning far more workers than physical CPU cores "
            "increases context-switching overhead, causes I/O contention, and can exhaust host memory or `/dev/shm` "
            "(`Bus error` / `Out of memory`)."
        ),
        "option_explanations": {
            "A": "Incorrect. PyTorch may emit a warning if `num_workers` exceeds suggested limits, but does not raise a `ValueError`.",
            "B": "Correct. Too many workers cause context switching, disk contention, and multiplied memory consumption across prefetched batch queues.",
            "C": "Incorrect. `batch_size` is never divided by `num_workers`; each worker produces full batches of size `batch_size`.",
            "D": "Incorrect. `DataLoader` workers run on the CPU and do not claim separate GPUs."
        },
        "competency": "Tune DataLoader num_workers based on CPU cores, I/O bandwidth, and host memory",
        "source": "LFD2001 Ch. 3"
    },

    # =========================================================================
    # D3: Transforms, Preprocessing, Data Splits, Data Leakage & Reproducibility
    # (PTCA-D-051 to PTCA-D-080, 30 questions)
    # =========================================================================
    {
        "id": "PTCA-D-051",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "What exact transformations does `torchvision.transforms.ToTensor()` perform when given an 8-bit RGB PIL "
            "Image (or `uint8` NumPy array) of height $H=224$, width $W=224$, and $C=3$ channels with pixel values in $[0, 255]$?"
        ),
        "code": (
            "import numpy as np\n"
            "from torchvision.transforms import ToTensor\n\n"
            "raw_img = np.random.randint(0, 256, size=(224, 224, 3), dtype=np.uint8)\n"
            "tensor_img = ToTensor()(raw_img)"
        ),
        "options": {
            "A": "It keeps shape `(224, 224, 3)` and converts `dtype` to `torch.float32` with values in `[0.0, 255.0]`.",
            "B": "It permutes dimensions from `(H, W, C)` to `(C, H, W) = (3, 224, 224)`, converts `dtype` to `torch.float32`, and scales pixel values from `[0, 255]` to `[0.0, 1.0]`.",
            "C": "It permutes dimensions to `(3, 224, 224)`, converts `dtype` to `torch.float32`, and standardizes values to zero mean and unit variance.",
            "D": "It adds a batch dimension `(1, 3, 224, 224)` and scales pixel values to `[-1.0, 1.0]`."
        },
        "correct": ["B"],
        "explanation": (
            "`torchvision.transforms.ToTensor()` converts a PIL Image or `numpy.ndarray` of shape `(H, W, C)` in the "
            "range `[0, 255]` (when `uint8` / common PIL modes) into a `torch.FloatTensor` (`torch.float32`) of shape "
            "`(C, H, W)` with values divided by `255.0` so they lie in `[0.0, 1.0]`."
        ),
        "option_explanations": {
            "A": "Incorrect. `ToTensor()` both permutes `(H, W, C)` to `(C, H, W)` and divides `uint8` values by `255.0`.",
            "B": "Correct. `ToTensor()` outputs a `torch.float32` tensor of shape `(C, H, W)` scaled to `[0.0, 1.0]`.",
            "C": "Incorrect. Zero-mean / unit-variance standardization requires `transforms.Normalize(mean, std)` after `ToTensor()`.",
            "D": "Incorrect. `ToTensor()` produces a 3D `(C, H, W)` tensor in `[0.0, 1.0]`, not a 4D tensor in `[-1.0, 1.0]`."
        },
        "competency": "Describe shape, dtype, and value scaling performed by torchvision.transforms.ToTensor()",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb & LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-052",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "A developer defines the `transforms.Compose` pipeline below and passes it to `datasets.CIFAR10(root='data', train=True, transform=pipeline)`. "
            "When `dataset[0]` is accessed, a `TypeError: img should be Tensor Image. Got <class 'PIL.Image.Image'>` is raised. Why?"
        ),
        "code": (
            "from torchvision import transforms\n\n"
            "pipeline = transforms.Compose([\n"
            "    transforms.Resize((32, 32)),\n"
            "    transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5)),\n"
            "    transforms.ToTensor(),\n"
            "])"
        ),
        "options": {
            "A": "`transforms.Resize` returns a NumPy array, which `Normalize` cannot accept.",
            "B": "`transforms.Normalize` only operates on a `torch.Tensor` (not a PIL Image), so `transforms.ToTensor()` must be placed BEFORE `transforms.Normalize` in `transforms.Compose`.",
            "C": "`transforms.Compose` executes its list of transforms in reverse order (bottom to top).",
            "D": "`CIFAR10` images have 1 channel, so `mean` and `std` must be 1-tuples `(0.5,)`."
        },
        "correct": ["B"],
        "explanation": (
            "`transforms.Compose` applies transforms sequentially in list order. `CIFAR10` yields a PIL Image, and "
            "`Resize((32, 32))` returns a resized PIL Image. Because `transforms.Normalize` is a tensor-only operation "
            "($x_{\\text{norm}} = (x - \\mu) / \\sigma$), calling it before `ToTensor()` raises a `TypeError`."
        ),
        "option_explanations": {
            "A": "Incorrect. `Resize` on a PIL Image returns a PIL Image, not a NumPy array.",
            "B": "Correct. `Normalize` requires a float Tensor image, so `ToTensor()` must precede `Normalize()` in the pipeline.",
            "C": "Incorrect. `transforms.Compose` executes transforms strictly from first to last (`for t in self.transforms: img = t(img)`).",
            "D": "Incorrect. `CIFAR10` consists of 3-channel RGB images; the error is caused by passing a PIL Image to `Normalize`."
        },
        "competency": "Order ToTensor() and Normalize() properly inside transforms.Compose()",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-053",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "An RGB image is converted by `transforms.ToTensor()` into a tensor with pixel values in $[0.0, 1.0]$, and "
            "then passed through `transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))`. What is the new "
            "minimum and maximum possible value range of the resulting tensor?"
        ),
        "code": (
            "from torchvision import transforms\n\n"
            "tf = transforms.Compose([\n"
            "    transforms.ToTensor(),\n"
            "    transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))\n"
            "])"
        ),
        "options": {
            "A": "`[0.0, 1.0]`",
            "B": "`[-0.5, 0.5]`",
            "C": "`[-1.0, 1.0]`",
            "D": "`[-2.0, 2.0]`"
        },
        "correct": ["C"],
        "explanation": (
            "`transforms.Normalize(mean, std)` computes $\\text{output}[c] = (\\text{input}[c] - \\text{mean}[c]) / \\text{std}[c]$ "
            "for each channel $c$. Given $\\text{input}[c] \\in [0.0, 1.0]$, $\\text{mean}[c] = 0.5$, and $\\text{std}[c] = 0.5$:\n"
            "- Minimum: $(0.0 - 0.5) / 0.5 = -1.0$\n"
            "- Maximum: $(1.0 - 0.5) / 0.5 = +1.0$\n"
            "Thus the output range is $[-1.0, 1.0]$."
        ),
        "option_explanations": {
            "A": "Incorrect. `[0.0, 1.0]` is the range after `ToTensor()` before `Normalize` is applied.",
            "B": "Incorrect. `[-0.5, 0.5]` only subtracts `mean=0.5` without dividing by `std=0.5`.",
            "C": "Correct. Applying $(x - 0.5) / 0.5$ maps $[0.0, 1.0]$ linearly onto $[-1.0, 1.0]$.",
            "D": "Incorrect. Reaching `[-2.0, 2.0]` would require `std=0.25`, not `0.5`."
        },
        "competency": "Calculate output value ranges produced by transforms.Normalize(mean, std)",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-054",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "When configuring `torchvision.transforms` for an image classification task, how should the `train_transform` "
            "(used on the training set) differ from the `val_test_transform` (used on the validation and test sets)?"
        ),
        "code": (
            "train_transform = transforms.Compose([\n"
            "    transforms.RandomResizedCrop(224),\n"
            "    transforms.RandomHorizontalFlip(p=0.5),\n"
            "    transforms.ToTensor(),\n"
            "    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])\n"
            "])\n"
            "val_test_transform = # How should this be defined?"
        ),
        "options": {
            "A": "`val_test_transform` should include only deterministic preprocessing (`Resize`, `CenterCrop`, `ToTensor`, and `Normalize` with the training set's `mean` and `std`), omitting stochastic data augmentations (`RandomResizedCrop`, `RandomHorizontalFlip`).",
            "B": "`val_test_transform` should use the exact same random augmentations as `train_transform` so the test distribution matches training.",
            "C": "`val_test_transform` should omit `Normalize` so test images are evaluated in raw `[0.0, 1.0]` space.",
            "D": "`val_test_transform` should compute and apply a separate `mean` and `std` fitted exclusively on the test set."
        },
        "correct": ["A"],
        "explanation": (
            "Stochastic data augmentations (`RandomResizedCrop`, `RandomHorizontalFlip`, `RandomRotation`, `ColorJitter`) "
            "artificially expand the training distribution to reduce overfitting, and must ONLY be applied to training "
            "data. Validation and test sets must use deterministic transforms (`Resize`/`CenterCrop`, `ToTensor`) and "
            "must be normalized using the exact same `mean` and `std` statistics learned from the training set."
        ),
        "option_explanations": {
            "A": "Correct. Evaluation uses deterministic spatial preprocessing and the training set's normalization parameters, without random augmentation.",
            "B": "Incorrect. Random augmentations during validation/testing introduce random variance into evaluation metrics and distort unaugmented real-world inputs.",
            "C": "Incorrect. Omitting `Normalize` at test time causes a severe covariate shift because the trained weights expect normalized inputs.",
            "D": "Incorrect. Computing normalization statistics on the test set is a form of data leakage and shifts the input scale relative to what the model was trained on."
        },
        "competency": "Separate stochastic training augmentations from deterministic validation/test transforms",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-055",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Hard",
        "multi_select": False,
        "stem": (
            "Carefully inspect the code below that splits a dataset with `random_split` and then assigns different "
            "transforms to `train_sub.dataset.transform` and `val_sub.dataset.transform`. What subtle bug occurs?"
        ),
        "code": (
            "from torch.utils.data import random_split\n"
            "from torchvision import datasets, transforms\n\n"
            "full_ds = datasets.ImageFolder('data/images')\n"
            "train_sub, val_sub = random_split(full_ds, [0.8, 0.2])\n\n"
            "train_sub.dataset.transform = transforms.Compose([\n"
            "    transforms.RandomHorizontalFlip(p=1.0),\n"
            "    transforms.ToTensor()\n"
            "])\n"
            "val_sub.dataset.transform = transforms.Compose([\n"
            "    transforms.ToTensor()\n"
            "])"
        ),
        "options": {
            "A": "`random_split` raises a `TypeError` when given float fractions `[0.8, 0.2]`.",
            "B": "`train_sub` and `val_sub` are `Subset` objects that both reference the SAME underlying `full_ds` instance (`train_sub.dataset is val_sub.dataset`), so the second assignment overwrites `full_ds.transform` and disables `RandomHorizontalFlip` on `train_sub` as well!",
            "C": "`val_sub` receives `RandomHorizontalFlip(p=1.0)` while `train_sub` receives only `ToTensor()`.",
            "D": "Assigning `.transform` after `random_split` reshuffles the indices between `train_sub` and `val_sub`."
        },
        "correct": ["B"],
        "explanation": (
            "`random_split(full_ds, ...)` returns two `torch.utils.data.Subset` wrappers that both hold a reference to "
            "the exact same `full_ds` object (`train_sub.dataset is val_sub.dataset is full_ds`). Mutating "
            "`val_sub.dataset.transform = ...` mutates `full_ds.transform`, overwriting the training transform! "
            "To use different transforms per split, either instantiate two separate `ImageFolder` instances with the "
            "same split `indices` passed to `Subset(train_full_ds, train_sub.indices)` and `Subset(val_full_ds, val_sub.indices)`, "
            "or wrap each `Subset` in a thin `Dataset` wrapper that applies its own `transform`."
        ),
        "option_explanations": {
            "A": "Incorrect. PyTorch's `random_split` natively supports float proportions that sum to `1.0` (e.g., `[0.8, 0.2]`) as well as integer lengths.",
            "B": "Correct. Both `Subset` instances point to the same underlying `full_ds` object, so the second `.dataset.transform` assignment overwrites the first for both splits.",
            "C": "Incorrect. Both `train_sub` and `val_sub` end up using the second assignment (`transforms.Compose([transforms.ToTensor()])`).",
            "D": "Incorrect. Modifying `.transform` does not alter `Subset.indices`."
        },
        "competency": "Identify and fix shared-dataset transform overwrite bugs after torch.utils.data.random_split",
        "source": "LFD2001 Ch. 4"
    },
])

QUESTIONS.extend([
    {
        "id": "PTCA-D-056",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "Review the tabular preprocessing workflow below. Why does this code introduce **data leakage** between "
            "the training and test sets?"
        ),
        "code": (
            "import torch\n"
            "from sklearn.preprocessing import StandardScaler\n"
            "from sklearn.model_selection import train_test_split\n\n"
            "scaler = StandardScaler()\n"
            "X_scaled = scaler.fit_transform(raw_features)\n"
            "X_train, X_test, y_train, y_test = train_test_split(\n"
            "    X_scaled, raw_targets, test_size=0.2, random_state=42\n"
            ")"
        ),
        "options": {
            "A": "Because `train_test_split` must be called with `shuffle=False` whenever `StandardScaler` is used.",
            "B": "Because `scaler.fit_transform(raw_features)` computes the feature means and standard deviations across the ENTIRE dataset (including the 20% test samples) before splitting, leaking test distribution statistics into the training features.",
            "C": "Because `StandardScaler` converts `float32` tensors into `float64` arrays, leaking precision.",
            "D": "Because `random_state=42` uses the same seed for both `X_train` and `X_test`."
        },
        "correct": ["B"],
        "explanation": (
            "Fitting a preprocessor (`scaler.fit_transform`) on the full dataset prior to `train_test_split` leaks "
            "information from the held-out test set into the mean $\\mu$ and standard deviation $\\sigma$ used to scale "
            "the training data. The correct workflow is to split first (`train_test_split`), then call "
            "`X_train = scaler.fit_transform(X_train)` and `X_test = scaler.transform(X_test)`."
        ),
        "option_explanations": {
            "A": "Incorrect. Shuffling during `train_test_split` (for i.i.d. data) does not cause leakage if scaling is performed after splitting.",
            "B": "Correct. Fitting `StandardScaler` on combined train + test data leaks test set statistics into training preprocessing.",
            "C": "Incorrect. Floating-point dtype precision is unrelated to statistical data leakage.",
            "D": "Incorrect. `random_state=42` makes the train/test partition reproducible, not leaky."
        },
        "competency": "Identify and prevent preprocessing data leakage when scaling features before train/test split",
        "source": "modules/module_6_pytorch_nn_hands_on/pytorch_nn_linear.ipynb & LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-057",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "How do you create a reproducible 80% / 20% train/validation split of a PyTorch `Dataset` using "
            "`torch.utils.data.random_split` without altering the global PyTorch RNG state?"
        ),
        "code": (
            "import torch\n"
            "from torch.utils.data import random_split\n\n"
            "# Reproducibly split full_dataset into 80% train and 20% val:"
        ),
        "options": {
            "A": "`random_split(full_dataset, [0.8, 0.2], generator=torch.Generator().manual_seed(42))`",
            "B": "`random_split(full_dataset, [0.8, 0.2], random_state=42)`",
            "C": "`random_split(full_dataset, [0.8, 0.2], seed=42)`",
            "D": "`random_split(full_dataset, test_size=0.2, shuffle=True)`"
        },
        "correct": ["A"],
        "explanation": (
            "`torch.utils.data.random_split(dataset, lengths, generator=default_generator)` accepts a `torch.Generator` "
            "via its `generator` keyword argument (`generator=torch.Generator().manual_seed(42)`). Unlike `scikit-learn`'s "
            "`train_test_split`, `random_split` does not have `random_state`, `seed`, or `test_size` parameters."
        ),
        "option_explanations": {
            "A": "Correct. Passing `generator=torch.Generator().manual_seed(42)` produces a deterministic split without mutating the global RNG.",
            "B": "Incorrect. `random_state` is a `scikit-learn` parameter (`train_test_split`), not a `torch.utils.data.random_split` parameter.",
            "C": "Incorrect. `random_split` does not accept a `seed` keyword argument.",
            "D": "Incorrect. `test_size` and `shuffle` belong to `sklearn.model_selection.train_test_split`."
        },
        "competency": "Create reproducible dataset partitions using torch.utils.data.random_split and torch.Generator",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-058",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "In `torchvision.datasets`, what is the purpose of the `target_transform` parameter (for example in "
            "`datasets.FashionMNIST(root='data', train=True, transform=..., target_transform=...)`)?"
        ),
        "code": (
            "from torchvision import datasets\n"
            "from torchvision.transforms import ToTensor, Lambda\n"
            "import torch\n\n"
            "ds = datasets.FashionMNIST(\n"
            "    root='data',\n"
            "    train=True,\n"
            "    transform=ToTensor(),\n"
            "    target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))\n"
            ")"
        ),
        "options": {
            "A": "It applies spatial geometric transforms to bounding-box coordinates inside the input image tensor.",
            "B": "It specifies a callable transformation applied exclusively to the sample's label/target `y` before `__getitem__` returns `(img, target)` (such as converting an integer class index into a one-hot float tensor).",
            "C": "It transforms the model's output logits after the forward pass.",
            "D": "It specifies the transform applied to the test set when `train=False`."
        },
        "correct": ["B"],
        "explanation": (
            "In `torchvision.datasets`, `transform` transforms the input feature (image), while `target_transform` "
            "transforms the target label `y` inside `__getitem__`. In the code shown, `Lambda(...)` with `.scatter_` "
            "converts an integer label `y` in `0..9` into a 10-element one-hot encoded `torch.float` vector."
        ),
        "option_explanations": {
            "A": "Incorrect. Joint image + bounding-box transforms require `torchvision.transforms.v2` on both inputs, whereas `target_transform` receives only the target `y`.",
            "B": "Correct. `target_transform` is a function/transform that takes in the target and transforms it (here, one-hot encoding).",
            "C": "Incorrect. `target_transform` runs inside `Dataset.__getitem__`, not on model outputs.",
            "D": "Incorrect. Test set feature transforms still use `transform=...` on the `train=False` dataset instance."
        },
        "competency": "Use target_transform and transforms.Lambda to transform dataset labels",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb & LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-059",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "What is the difference in output dimensions between `transforms.Resize(256)` (passing a single integer) "
            "and `transforms.Resize((256, 256))` (passing a 2-tuple) when applied to a rectangular image of size "
            "$(H, W) = (600, 300)$?"
        ),
        "code": (
            "from torchvision import transforms\n\n"
            "# Input image has height H=600, width W=300\n"
            "t_int = transforms.Resize(256)\n"
            "t_tup = transforms.Resize((256, 256))"
        ),
        "options": {
            "A": "Both produce a `(256, 256)` square image; there is no difference.",
            "B": "`Resize(256)` rescales the *smaller* edge to `256` while preserving aspect ratio (producing height `512`, width `256`), whereas `Resize((256, 256))` forces both height and width to `(256, 256)` without preserving aspect ratio.",
            "C": "`Resize(256)` rescales the *larger* edge to `256` (producing height `256`, width `128`), whereas `Resize((256, 256))` center-crops the image.",
            "D": "`Resize(256)` raises a `TypeError` because `size` must always be a 2-tuple `(H, W)`."
        },
        "correct": ["B"],
        "explanation": (
            "In `torchvision.transforms.Resize(size)`, if `size` is a sequence `(h, w)`, the output image is matched "
            "directly to `(h, w)` (stretching if aspect ratio differs). If `size` is a single `int`, the smaller edge "
            "of the image is matched to `size` while maintaining the aspect ratio: since $H > W$ ($600 > 300$), the "
            "output becomes `(size * H / W, size) = (512, 256)`. (Note: this is why `Resize(256)` is almost always "
            "followed by `CenterCrop(224)` or `RandomCrop(224)` before batching!)"
        ),
        "option_explanations": {
            "A": "Incorrect. Passing a single integer preserves aspect ratio, so rectangular images remain rectangular.",
            "B": "Correct. `Resize(int)` scales the shorter side to `256` preserving aspect ratio `(512, 256)`, while `Resize((256, 256))` warps to an exact square.",
            "C": "Incorrect. By default (when `max_size=None`), `Resize(int)` matches the *shorter* edge, not the longer edge.",
            "D": "Incorrect. `Resize` accepts either an `int` or a `(h, w)` sequence."
        },
        "competency": "Distinguish aspect-ratio-preserving Resize(int) from fixed-dimension Resize((H, W))",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-060",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Hard",
        "multi_select": False,
        "stem": (
            "A custom `Dataset.__getitem__` uses `numpy.random` (or Python's `random` module) to apply random noise "
            "to each sample. Even though `torch.manual_seed(42)` is called in the main script, how should worker seeding "
            "be configured in `DataLoader(..., num_workers=4)` so that external RNGs (`numpy.random`, `random`) do NOT "
            "produce identical random sequences across forked worker processes or across runs?"
        ),
        "code": (
            "import random\n"
            "import numpy as np\n"
            "import torch\n"
            "from torch.utils.data import DataLoader\n\n"
            "def seed_worker(worker_id):\n"
            "    worker_seed = torch.initial_seed() % 2**32\n"
            "    np.random.seed(worker_seed)\n"
            "    random.seed(worker_seed)\n\n"
            "g = torch.Generator()\n"
            "g.manual_seed(42)\n"
            "loader = DataLoader(ds, batch_size=32, num_workers=4, worker_init_fn=seed_worker, generator=g)"
        ),
        "options": {
            "A": "Pass a `worker_init_fn` that seeds `numpy.random` and `random` using `torch.initial_seed() % 2**32` (where each worker's PyTorch seed is `base_seed + worker_id`), along with a seeded `generator` on `DataLoader`.",
            "B": "Call `np.random.seed(42)` inside `seed_worker(worker_id)` with the exact same constant `42` for every worker.",
            "C": "Set `shuffle=False` because worker seeding only works when `shuffle=False`.",
            "D": "PyTorch automatically seeds `numpy.random` with `42 + worker_id` in all versions of Python without `worker_init_fn`."
        },
        "correct": ["A"],
        "explanation": (
            "In `DataLoader`, each worker process has its PyTorch seed initialized to `base_seed + worker_id` (accessible "
            "via `torch.initial_seed()`). However, if workers are created via `fork` without re-seeding `numpy.random`, "
            "all workers inherit the exact same `numpy.random` state and generate identical random augmentations! "
            "Defining `worker_init_fn` to seed `np.random.seed(torch.initial_seed() % 2**32)` and `random.seed(...)` "
            "(combined with `generator=g`) ensures each worker has a distinct yet fully reproducible RNG stream."
        ),
        "option_explanations": {
            "A": "Correct. Using `torch.initial_seed() % 2**32` inside `worker_init_fn` gives each worker a unique, deterministic seed derived from `base_seed + worker_id`.",
            "B": "Incorrect. Seeding every worker with the constant `42` forces all 4 workers to generate identical random numbers!",
            "C": "Incorrect. `worker_init_fn` and `generator` work together with `shuffle=True`.",
            "D": "Incorrect. PyTorch seeds its own `torch` RNG per worker (`base_seed + worker_id`), not third-party RNGs like `numpy.random` in forked processes."
        },
        "competency": "Configure worker_init_fn and generator in DataLoader for reproducible multi-worker augmentation",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-061",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "You have a medical imaging dataset of 5,000 chest X-rays taken from 500 patients (10 X-rays per patient "
            "at slightly different angles). You split the 5,000 images into 4,000 train and 1,000 validation images "
            "using `torch.utils.data.random_split(dataset, [4000, 1000])`. Validation accuracy reaches 99%, but accuracy "
            "on a new hospital's patients drops to 68%. What caused the inflated validation accuracy?"
        ),
        "code": (
            "# 5000 images from 500 patients (10 images per patient)\n"
            "train_ds, val_ds = random_split(xray_dataset, [4000, 1000])"
        ),
        "options": {
            "A": "`random_split` did not shuffle the images before splitting.",
            "B": "**Group / subject-level data leakage**: random image-level splitting placed near-duplicate X-rays from the *same patient* into both `train_ds` and `val_ds`, allowing the model to memorize patient-specific anatomy instead of learning generalizable pathology.",
            "C": "The validation split of 1,000 images is too large relative to the 4,000 training images.",
            "D": "`random_split` normalized the validation images using training statistics."
        },
        "correct": ["B"],
        "explanation": (
            "When multiple samples belong to the same underlying entity or group (such as multiple scans per patient, "
            "frames from the same video clip, or recordings from the same speaker), an image-level `random_split` leaks "
            "subject identity across splits. Splitting must be performed at the *patient/group* level (e.g., `GroupShuffleSplit` "
            "or `StratifiedGroupKFold`) so all images from a given patient reside strictly in one split."
        ),
        "option_explanations": {
            "A": "Incorrect. `random_split` does shuffle at the sample level, which is precisely why samples from the same patient end up in both splits.",
            "B": "Correct. Splitting at the image level instead of the patient/group level causes subject leakage across train and validation sets.",
            "C": "Incorrect. An 80/20 split is standard and does not inflate validation accuracy.",
            "D": "Incorrect. Normalizing validation images with training statistics is proper practice, and `random_split` does not perform normalization."
        },
        "competency": "Detect group/subject-level data leakage when splitting datasets with repeated measurements",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-062",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "You are building a fraud detection classifier on a dataset where 99% of transactions are legitimate (`0`) "
            "and only 1% are fraudulent (`1`). When splitting into train and test sets with `sklearn.model_selection.train_test_split`, "
            "which argument ensures that both splits preserve the exact 99% / 1% class ratio?"
        ),
        "code": (
            "from sklearn.model_selection import train_test_split\n\n"
            "X_train, X_test, y_train, y_test = train_test_split(\n"
            "    X, y, test_size=0.2, random_state=42, ???\n"
            ")"
        ),
        "options": {
            "A": "`stratify=y`",
            "B": "`balanced=True`",
            "C": "`weights=y`",
            "D": "`shuffle=False`"
        },
        "correct": ["A"],
        "explanation": (
            "Passing `stratify=y` to `train_test_split` performs stratified sampling, ensuring that the class distribution "
            "of `y` is preserved identically in both `y_train` and `y_test`—critical for imbalanced datasets where a "
            "purely uniform random split could leave very few (or zero) minority-class examples in the validation/test split."
        ),
        "option_explanations": {
            "A": "Correct. `stratify=y` preserves the target class proportions across the train and test splits.",
            "B": "Incorrect. `train_test_split` does not have a `balanced` argument.",
            "C": "Incorrect. `train_test_split` does not have a `weights` argument.",
            "D": "Incorrect. `shuffle=False` splits by array order without stratifying class proportions."
        },
        "competency": "Use stratified splitting (stratify=y) to preserve class distributions on imbalanced datasets",
        "source": "modules/module_6_pytorch_nn_hands_on/pytorch_nn_linear.ipynb & LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-063",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "You are training a time-series forecasting model on hourly electricity demand recorded from January 2023 "
            "to December 2025. Why is applying `torch.utils.data.random_split` (or `train_test_split(..., shuffle=True)`) "
            "across all hourly timestamps a severe methodological error?"
        ),
        "code": (
            "# Hourly time-series records ordered chronologically from 2023 to 2025:\n"
            "train_ds, test_ds = random_split(timeseries_ds, [0.8, 0.2])"
        ),
        "options": {
            "A": "Because `random_split` only works on 2D image tensors, not 1D time-series tensors.",
            "B": "Because random splitting causes **temporal (look-ahead) data leakage**: the model trains on future timestamps (e.g., 2:00 PM and 4:00 PM on a given day in 2025) and is evaluated on intermediate past timestamps (e.g., 3:00 PM on that same day).",
            "C": "Because time-series models require the test set to come chronologically *before* the training set.",
            "D": "Because `random_split` changes the sampling frequency of the timestamps."
        },
        "correct": ["B"],
        "explanation": (
            "For chronological time-series forecasting, randomly assigning timestamps to train and test sets causes "
            "temporal (look-ahead) leakage: strongly autocorrelated adjacent hours from the future are present in the "
            "training set, allowing the model to interpolate rather than forecast. Time-series splits must be chronological "
            "(e.g., train on 2023–2024, validate on early 2025, test on late 2025)."
        ),
        "option_explanations": {
            "A": "Incorrect. `random_split` works on any map-style `Dataset` regardless of tensor dimensionality.",
            "B": "Correct. Random splitting across time leaks future observations and autocorrelation into the training set.",
            "C": "Incorrect. In forecasting, the validation and test windows must come chronologically *after* the training window.",
            "D": "Incorrect. `random_split` subsets indices and does not resample signal frequency."
        },
        "competency": "Prevent temporal look-ahead data leakage when splitting time-series datasets",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-064",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "In `torchvision.transforms`, why does passing `transforms.RandomErasing(p=0.5)` BEFORE `transforms.ToTensor()` "
            "in `transforms.Compose` raise a `TypeError`?"
        ),
        "code": (
            "from torchvision import transforms\n\n"
            "tf = transforms.Compose([\n"
            "    transforms.RandomHorizontalFlip(p=0.5),\n"
            "    transforms.RandomErasing(p=0.5),\n"
            "    transforms.ToTensor()\n"
            "])"
        ),
        "options": {
            "A": "Because `RandomErasing` is a Tensor-only transform (like `Normalize`) and cannot operate on a PIL Image; it must be placed *after* `ToTensor()`.",
            "B": "Because `RandomErasing` cannot be combined with `RandomHorizontalFlip` in the same pipeline.",
            "C": "Because `RandomErasing` requires a 4D batch tensor and can only be run inside `collate_fn`.",
            "D": "Because `p=0.5` is invalid; `RandomErasing` requires an integer percentage `p=50`."
        },
        "correct": ["A"],
        "explanation": (
            "In classic `torchvision.transforms`, most geometric/color transforms (`Resize`, `RandomCrop`, "
            "`RandomHorizontalFlip`, `ColorJitter`) accept either PIL Images or Tensor images, whereas `Normalize` and "
            "`RandomErasing` operate *strictly* on `torch.Tensor` images (`(C, H, W)` or `(B, C, H, W)`) and must be "
            "placed after `ToTensor()`."
        ),
        "option_explanations": {
            "A": "Correct. `RandomErasing` expects a `torch.Tensor` image and fails with `TypeError` if given a PIL Image prior to `ToTensor()`.",
            "B": "Incorrect. `RandomErasing` and `RandomHorizontalFlip` are routinely used together when ordered properly.",
            "C": "Incorrect. `RandomErasing` operates on individual `(C, H, W)` image tensors after `ToTensor()`.",
            "D": "Incorrect. Probability `p` in `torchvision.transforms` is a float in `[0.0, 1.0]`."
        },
        "competency": "Distinguish PIL-compatible transforms from Tensor-only transforms (Normalize, RandomErasing)",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-065",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "You are training a handwritten digit classifier (`MNIST` / digit recognition where `'6'` and `'9'` are "
            "distinct classes, or directional traffic sign recognition where `'Turn Left'` and `'Turn Right'` are "
            "distinct classes). Which data augmentation transform will corrupt label semantics and hurt accuracy?"
        ),
        "code": (
            "train_tf = transforms.Compose([\n"
            "    transforms.RandomVerticalFlip(p=0.5),\n"
            "    transforms.RandomHorizontalFlip(p=0.5),\n"
            "    transforms.ToTensor()\n"
            "])"
        ),
        "options": {
            "A": "Only `ToTensor()`, because scaling to `[0.0, 1.0]` erases edge direction.",
            "B": "`RandomHorizontalFlip` and `RandomVerticalFlip`, because flipping a directional traffic sign (`'Turn Left'`) or asymmetric digit (`'6'`, `'2'`, `'5'`) changes its true semantic class while keeping the original label unchanged.",
            "C": "Small `ColorJitter(brightness=0.1, contrast=0.1)`, because lighting changes alter digit identity.",
            "D": "Data augmentation never affects label semantics in classification tasks."
        },
        "correct": ["B"],
        "explanation": (
            "Data augmentations must be *label-preserving* symmetries of the domain. While horizontal flips preserve "
            "natural object classes (`cat`, `dog`, `shirt` in FashionMNIST), flipping digits (`6` $\\leftrightarrow$ `9` "
            "under rotation/flips, or mirror-reversed `3`) or directional signs (`Left` $\\leftrightarrow$ `Right`) changes "
            "the ground-truth meaning or produces out-of-distribution symbols while the label remains fixed."
        ),
        "option_explanations": {
            "A": "Incorrect. `ToTensor()` is a lossless linear scaling of pixel intensities.",
            "B": "Correct. Augmentations must preserve the target label; horizontal/vertical flips violate label invariance on digits and directional signs.",
            "C": "Incorrect. Mild brightness/contrast jitter preserves digit and sign identity.",
            "D": "Incorrect. Any transformation that alters the semantic class without updating the target label introduces label noise."
        },
        "competency": "Select domain-appropriate, label-preserving data augmentations",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-066",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "A tabular dataset has missing (`NaN`) values in 8% of the rows of a continuous column `'income'`. "
            "You impute missing values using the median of `'income'`. To prevent data leakage, how must median "
            "imputation be performed across the train, validation, and test sets?"
        ),
        "code": (
            "# X_train, X_val, X_test have already been split\n"
            "# Column 2 ('income') contains float('nan') entries in all three splits"
        ),
        "options": {
            "A": "Compute a single median across `concat(X_train, X_val, X_test)` and fill `NaN`s in all three splits with that global median.",
            "B": "Compute `train_median = torch.nanmedian(X_train[:, 2]).values` on `X_train` ONLY, and use `train_median` to fill `NaN`s in `X_train`, `X_val`, and `X_test`.",
            "C": "Compute three separate medians (`train_median`, `val_median`, `test_median`) independently on each split, even when `X_test` has only 1 sample at inference time.",
            "D": "Replace `NaN`s in `X_train` with `0.0` and leave `NaN`s untouched in `X_val` and `X_test`."
        },
        "correct": ["B"],
        "explanation": (
            "Just like normalization (`mean`/`std`), imputation statistics (mean, median, mode) are learned parameters "
            "of the preprocessing pipeline. They must be computed *exclusively* on the training split (`X_train`) and "
            "then applied unchanged to fill missing values in `X_train`, `X_val`, and `X_test` (including single-sample "
            "production inference where a test-set median cannot even be defined)."
        ),
        "option_explanations": {
            "A": "Incorrect. Computing the median on combined train/val/test data leaks validation and test distributions into training.",
            "B": "Correct. Imputation parameters are fitted on `X_train` only and applied consistently to `X_train`, `X_val`, and `X_test`.",
            "C": "Incorrect. Fitting separate statistics on the test set leaks test distribution properties and fails for single-sample online inference.",
            "D": "Incorrect. Leaving `NaN` values in `X_val` or `X_test` causes `model(X)` to output `NaN` for every neuron connected to that feature."
        },
        "competency": "Impute missing values (NaNs) without leaking validation or test statistics",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-067",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "What happens during training if even a single input feature in a minibatch `X` of shape `(64, 10)` contains "
            "`float('nan')` when passed through a standard `nn.Linear(10, 64)` layer and `nn.MSELoss()`, followed by "
            "`loss.backward()` and `optimizer.step()`?"
        ),
        "code": (
            "X = torch.randn(64, 10)\n"
            "X[3, 5] = float('nan')  # One uncleaned missing value\n"
            "pred = model(X)\n"
            "loss = criterion(pred, Y)\n"
            "loss.backward()\n"
            "optimizer.step()"
        ),
        "options": {
            "A": "PyTorch's `nn.Linear` automatically ignores `NaN` entries and computes the dot product over the remaining 9 features.",
            "B": "The `NaN` propagates to `pred[3]`, turns the scalar `loss` into `nan`, produces `nan` gradients during `loss.backward()`, and corrupts the model's weights to `nan` upon `optimizer.step()`.",
            "C": "`MSELoss` clips `NaN` values to `0.0` and logs a warning.",
            "D": "Only sample 3's prediction is `nan`, while `loss` and the model weights remain finite."
        },
        "correct": ["B"],
        "explanation": (
            "IEEE 754 floating-point arithmetic propagates `NaN` (`nan + x = nan`, `nan * w = nan`). A single `NaN` in "
            "`X[3, 5]` makes `pred[3]` all `NaN`, which makes the reduced scalar `loss` `NaN`. Backpropagating a `NaN` "
            "loss fills parameter gradients with `NaN`, and `optimizer.step()` permanently corrupts the model parameters "
            "with `NaN`. Detecting (`torch.isnan(X).any()`) and imputing/filtering `NaN`s during preprocessing is essential."
        ),
        "option_explanations": {
            "A": "Incorrect. `nn.Linear` performs standard matrix multiplication where any `NaN` operand yields `NaN`.",
            "B": "Correct. One `NaN` in a batch contaminates the scalar loss, gradients, and all updated model weights.",
            "C": "Incorrect. `MSELoss` does not sanitize or clip `NaN` inputs.",
            "D": "Incorrect. Because `MSELoss` sums/averages over all 64 samples in the batch, `pred[3] = nan` makes the entire scalar `loss` `nan`."
        },
        "competency": "Trace how unhandled NaN values in input tensors corrupt loss and model parameters",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-068",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Hard",
        "multi_select": False,
        "stem": (
            "You want to split a single `datasets.ImageFolder('data/pets')` into an 80% training set (with random "
            "augmentations `train_tf`) and a 20% validation set (with deterministic `val_tf`) WITHOUT mutating a shared "
            "`.transform` attribute. Which of the following patterns cleanly achieves this?"
        ),
        "code": (
            "import torch\n"
            "from torch.utils.data import Subset\n"
            "from torchvision import datasets\n\n"
            "# Goal: 80/20 split with distinct train_tf and val_tf and zero overlap"
        ),
        "options": {
            "A": (
                "Instantiate `train_full = datasets.ImageFolder('data/pets', transform=train_tf)` and "
                "`val_full = datasets.ImageFolder('data/pets', transform=val_tf)`, generate one random permutation "
                "`perm = torch.randperm(len(train_full), generator=g).tolist()`, and create "
                "`Subset(train_full, perm[:n_train])` and `Subset(val_full, perm[n_train:])`."
            ),
            "B": (
                "Call `random_split` twice independently: `train_ds, _ = random_split(ImageFolder('data/pets', train_tf), [0.8, 0.2])` "
                "and `_, val_ds = random_split(ImageFolder('data/pets', val_tf), [0.8, 0.2])` without a shared generator."
            ),
            "C": (
                "Pass `transform=[train_tf, val_tf]` directly to `random_split(full_ds, [0.8, 0.2])`."
            ),
            "D": (
                "Apply `train_tf` to both splits during data loading and call `model.eval()` to disable `RandomHorizontalFlip`."
            )
        },
        "correct": ["A"],
        "explanation": (
            "By creating two lightweight `ImageFolder` instances (`train_full` with `train_tf` and `val_full` with `val_tf`, "
            "which only scan file paths in `__init__`) and slicing a single shared index permutation `perm` into disjoint "
            "`perm[:n_train]` and `perm[n_train:]` passed to `Subset`, you guarantee both disjoint train/val indices "
            "and completely independent transform pipelines."
        ),
        "option_explanations": {
            "A": "Correct. Using disjoint slices of a single index permutation on two `ImageFolder` instances with distinct `transform`s prevents both transform overwrite and sample overlap.",
            "B": "Incorrect. Calling `random_split` twice without identical seeds produces two different random permutations, causing training samples to leak into `val_ds`!",
            "C": "Incorrect. `random_split` does not accept a `transform` argument.",
            "D": "Incorrect. `model.eval()` only affects `nn.Module` layers (`Dropout`, `BatchNorm`), NOT `torchvision.transforms` inside `Dataset.__getitem__`!"
        },
        "competency": "Apply distinct train and validation transforms to disjoint Subset splits without leakage",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-069",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "A common misconception is that calling `model.eval()` before running the validation loop automatically "
            "disables random data augmentations such as `transforms.RandomHorizontalFlip(p=0.5)` inside the validation "
            "`DataLoader`. Why is this FALSE?"
        ),
        "code": (
            "model.eval()\n"
            "with torch.no_grad():\n"
            "    for x, y in val_loader:  # val_loader's dataset has RandomHorizontalFlip(p=0.5)\n"
            "        preds = model(x)"
        ),
        "options": {
            "A": "`model.eval()` only sets `self.training = False` on the `nn.Module` hierarchy (affecting layers like `nn.Dropout` and `nn.BatchNorm2d`); the `Dataset` and its `torchvision.transforms` have no reference to `model` and continue applying `RandomHorizontalFlip` on every sample.",
            "B": "`torch.no_grad()` re-enables `RandomHorizontalFlip` whenever gradients are disabled.",
            "C": "`model.eval()` only disables `RandomHorizontalFlip` when `num_workers=0`.",
            "D": "You must call `val_loader.eval()` to disable `RandomHorizontalFlip`."
        },
        "correct": ["A"],
        "explanation": (
            "As emphasized in Module 4 (`pytorch_data_utilities.ipynb`), `Dataset`/`DataLoader` are completely decoupled "
            "from `nn.Module`. Calling `model.eval()` only toggles `training=False` on `model` and its child `nn.Module` "
            "layers; it has zero effect on the `Dataset`'s `transform` pipeline, nor does `DataLoader` have an `.eval()` method."
        ),
        "option_explanations": {
            "A": "Correct. `model.eval()` only affects `nn.Module` layers; dataset transforms execute independently inside `Dataset.__getitem__`.",
            "B": "Incorrect. `torch.no_grad()` only disables autograd graph construction and has no connection to image transforms.",
            "C": "Incorrect. `model.eval()` never communicates with `Dataset` transforms regardless of `num_workers`.",
            "D": "Incorrect. `DataLoader` has no `.eval()` method."
        },
        "competency": "Explain why model.eval() does not disable stochastic torchvision transforms in a Dataset",
        "source": "modules/module_4_working_with_data/pytorch_data_utilities.ipynb & LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-070",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "In `torchvision.transforms.v2`, what is the recommended replacement for the legacy `transforms.ToTensor()` "
            "when converting a PIL Image or `uint8` image into a float32 tensor scaled to $[0.0, 1.0]$?"
        ),
        "code": (
            "from torchvision.transforms import v2\n"
            "import torch\n\n"
            "# Modern torchvision.transforms.v2 equivalent of transforms.ToTensor():"
        ),
        "options": {
            "A": "`v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])`",
            "B": "`v2.Compose([v2.ToPILImage(), v2.ToDtype(torch.uint8, scale=False)])`",
            "C": "`v2.Normalize(mean=[0.0], std=[255.0])`",
            "D": "`v2.ToFloat64(scale=False)`"
        },
        "correct": ["A"],
        "explanation": (
            "In `torchvision.transforms.v2`, `ToTensor()` is deprecated in favor of separating container conversion "
            "from dtype/value scaling: `v2.ToImage()` converts a PIL Image or NumPy array to a `tv_tensors.Image` (preserving "
            "`uint8` dtype in `[0, 255]`, which is faster for geometric transforms), followed by "
            "`v2.ToDtype(torch.float32, scale=True)` to convert to `float32` and scale values to `[0.0, 1.0]`."
        ),
        "option_explanations": {
            "A": "Correct. `v2.ToImage()` followed by `v2.ToDtype(torch.float32, scale=True)` is the canonical `v2` replacement for `ToTensor()`.",
            "B": "Incorrect. `ToPILImage()` converts a tensor back to a PIL Image, and `torch.uint8` does not produce a float32 tensor.",
            "C": "Incorrect. `Normalize` requires a floating-point tensor input and cannot run directly on a `uint8` tensor or PIL Image.",
            "D": "Incorrect. `v2.ToFloat64` does not exist, and PyTorch models expect `float32`."
        },
        "competency": "Use modern torchvision.transforms.v2 (ToImage and ToDtype) pipelines",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-071",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "Suppose you compute per-channel mean and standard deviation across your RGB training set of shape "
            "`(N, 3, H, W)` (after `ToTensor()`). Which tensor reduction dimensions `dim=...` compute the exact "
            "3-element vector of channel means `(mean_R, mean_G, mean_B)` across all samples and spatial pixels?"
        ),
        "code": (
            "# X_train_images has shape (5000, 3, 32, 32) and dtype float32 in [0.0, 1.0]\n"
            "channel_mean = X_train_images.mean(dim=???)\n"
            "channel_std = X_train_images.std(dim=???)"
        ),
        "options": {
            "A": "`dim=(0, 2, 3)`",
            "B": "`dim=1`",
            "C": "`dim=(1, 2, 3)`",
            "D": "`dim=0`"
        },
        "correct": ["A"],
        "explanation": (
            "For a 4D image batch/dataset tensor of shape `(N, C, H, W) = (5000, 3, 32, 32)`, dimension `1` is the "
            "channel dimension `C=3`. Reducing over `dim=(0, 2, 3)` averages across all `N=5000` images, `H=32` rows, "
            "and `W=32` columns while leaving dimension `1` intact, producing a 1D tensor of shape `(3,)` ready for "
            "`transforms.Normalize(mean=channel_mean, std=channel_std)`."
        ),
        "option_explanations": {
            "A": "Correct. Reducing along batch (`0`), height (`2`), and width (`3`) leaves the channel dimension (`1`) of size `3`.",
            "B": "Incorrect. `dim=1` averages across the RGB channels and returns a tensor of shape `(5000, 32, 32)`.",
            "C": "Incorrect. `dim=(1, 2, 3)` computes one scalar mean per image, returning shape `(5000,)`.",
            "D": "Incorrect. `dim=0` computes a per-pixel mean image of shape `(3, 32, 32)`."
        },
        "competency": "Compute per-channel normalization statistics (mean and std) across (N, C, H, W) training tensors",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-072",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": True,
        "stem": (
            "In a binary or multi-class classification problem with severe class imbalance (e.g., 95% class `0`, 5% class `1`), "
            "which TWO PyTorch techniques address the imbalance without causing data leakage?"
        ),
        "code": "",
        "options": {
            "A": "Pass a per-sample weight vector derived from the training set's inverse class counts to `WeightedRandomSampler(..., replacement=True)` on the training `DataLoader`.",
            "B": "Pass class weights derived from the training set to the loss function (e.g., `nn.CrossEntropyLoss(weight=class_weights)` or `nn.BCEWithLogitsLoss(pos_weight=...)`).",
            "C": "Duplicate minority-class samples across the entire dataset *before* calling `random_split(dataset, [0.8, 0.2])`.",
            "D": "Apply `WeightedRandomSampler` to the test `DataLoader` so test accuracy is evaluated on an artificially 50/50 balanced test set."
        },
        "correct": ["A", "B"],
        "explanation": (
            "Class imbalance can be addressed at the data-sampling level on the training split via `WeightedRandomSampler` "
            "or at the loss level via `nn.CrossEntropyLoss(weight=...)` / `nn.BCEWithLogitsLoss(pos_weight=...)`, "
            "using class frequencies computed strictly on the training split. Oversampling/duplicating "
            "minority samples *before* `random_split` places exact duplicate copies of the same minority sample "
            "in both train and validation sets (severe data leakage!). Modifying the test `DataLoader` with `WeightedRandomSampler` "
            "distorts the true test distribution."
        ),
        "option_explanations": {
            "A": "Correct. Oversampling minority classes in the training `DataLoader` via `WeightedRandomSampler` balances training minibatches cleanly.",
            "B": "Correct. Weighting the loss function by inverse class frequency penalizes minority-class errors proportionally during training.",
            "C": "Incorrect. Duplicating minority samples before splitting places identical copies in both train and validation splits, causing severe data leakage.",
            "D": "Incorrect. Validation and test sets should reflect the true target evaluation distribution (or use class-balanced metrics like macro-F1 / PR-AUC) rather than random resampling."
        },
        "competency": "Handle class imbalance using WeightedRandomSampler or weighted loss without data leakage",
        "source": "LFD2001 Ch. 3 & Ch. 4"
    },
    {
        "id": "PTCA-D-073",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "Why is a three-way dataset split (**Training / Validation / Test**) necessary when tuning hyperparameters "
            "(such as learning rate, weight decay, and network depth) instead of tuning directly on a two-way "
            "(**Training / Test**) split?"
        ),
        "code": "",
        "options": {
            "A": "Because PyTorch's `DataLoader` requires at least three `Dataset` instances to initialize `num_workers`.",
            "B": "Because repeatedly selecting hyperparameters, architectures, or early-stopping checkpoints based on test-set performance leaks information from the test set into model design decisions, causing the model to overfit the test set and yield overly optimistic generalization estimates.",
            "C": "Because gradients are backpropagated on both the training and validation sets during `loss.backward()`.",
            "D": "Because `random_split` only accepts a list of 3 lengths `[train_len, val_len, test_len]`."
        },
        "correct": ["B"],
        "explanation": (
            "Every time you evaluate on a dataset and use that feedback to choose hyperparameters, architectures, or "
            "early-stopping epochs, degrees of freedom are fit to that dataset. A dedicated **validation set** absorbs "
            "this hyperparameter selection process, while the held-out **test set** is evaluated only once at the very "
            "end to provide an unbiased estimate of generalization performance."
        ),
        "option_explanations": {
            "A": "Incorrect. Each `DataLoader` wraps a single `Dataset` independently.",
            "B": "Correct. Tuning hyperparameters or early stopping on the test set causes indirect data leakage (information leakage into model selection), biasing the final test metric.",
            "C": "Incorrect. Gradients are never backpropagated on the validation set (`model.eval()` + `with torch.no_grad():`).",
            "D": "Incorrect. `random_split` accepts a sequence of any number of split lengths."
        },
        "competency": "Explain the distinct roles of training, validation, and test splits in preventing model-selection leakage",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-074",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "You have a normalized image tensor `norm_img` of shape `(3, 224, 224)` that was normalized with "
            "`transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])`. How do you mathematically "
            "invert (un-normalize) `norm_img` back to the `[0.0, 1.0]` range for visualization with `plt.imshow`?"
        ),
        "code": (
            "mean = torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)\n"
            "std = torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)\n"
            "# Given norm_img = (img - mean) / std, recover img in [0.0, 1.0]:"
        ),
        "options": {
            "A": "`img = (norm_img + mean) * std`",
            "B": "`img = norm_img * std + mean`",
            "C": "`img = (norm_img - mean) * std`",
            "D": "`img = norm_img / std - mean`"
        },
        "correct": ["B"],
        "explanation": (
            "Since `Normalize` computes $x_{\\text{norm}} = \\frac{x - \\mu}{\\sigma}$, solving for $x$ gives "
            "$x = x_{\\text{norm}} \\cdot \\sigma + \\mu$. Reshaping `mean` and `std` to `(3, 1, 1)` allows clean "
            "broadcasting across the spatial dimensions `(3, 224, 224)`."
        ),
        "option_explanations": {
            "A": "Incorrect. Adding `mean` before multiplying by `std` yields $x_{\\text{norm}}\\sigma + \\mu\\sigma \\neq x$.",
            "B": "Correct. Multiplying by `std` first and then adding `mean` ($x_{\\text{norm}} \\cdot \\sigma + \\mu$) exactly inverts $(x - \\mu) / \\sigma$.",
            "C": "Incorrect. Subtracting `mean` and multiplying by `std` does not invert the linear transformation.",
            "D": "Incorrect. Dividing by `std` compounds the scaling instead of inverting it."
        },
        "competency": "Invert channel-wise transforms.Normalize for image visualization",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-075",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "When writing a custom transformation class to pass inside `transforms.Compose([..., AddGaussianNoise(0.0, 0.1)])`, "
            "which special method must `AddGaussianNoise` implement (assuming it does not subclass `nn.Module`) so that "
            "`transforms.Compose` can invoke it on each sample?"
        ),
        "code": (
            "import torch\n\n"
            "class AddGaussianNoise:\n"
            "    def __init__(self, mean=0.0, std=0.1):\n"
            "        self.mean = mean\n"
            "        self.std = std\n\n"
            "    # Which method makes instances callable by transforms.Compose?"
        ),
        "options": {
            "A": "`def __call__(self, tensor): return tensor + torch.randn_like(tensor) * self.std + self.mean`",
            "B": "`def __getitem__(self, tensor): return tensor + torch.randn_like(tensor) * self.std + self.mean`",
            "C": "`def transform(self, tensor): return tensor + torch.randn_like(tensor) * self.std + self.mean`",
            "D": "`def __iter__(self, tensor): return tensor + torch.randn_like(tensor) * self.std + self.mean`"
        },
        "correct": ["A"],
        "explanation": (
            "`transforms.Compose` loops over `self.transforms` and invokes each transform as a callable `img = t(img)`. "
            "Implementing `__call__(self, tensor)` on a custom Python class (or subclassing `nn.Module` and implementing "
            "`forward(self, tensor)`, since `nn.Module.__call__` invokes `forward`) makes the instance callable."
        ),
        "option_explanations": {
            "A": "Correct. Implementing `__call__(self, tensor)` allows `transforms.Compose` to call `t(img)` on each sample.",
            "B": "Incorrect. `__getitem__` is for bracket indexing `obj[idx]`, not function call syntax `obj(img)`.",
            "C": "Incorrect. `transforms.Compose` calls `t(img)`, not `t.transform(img)`.",
            "D": "Incorrect. `__iter__` is for iteration, not callable transforms."
        },
        "competency": "Write custom callable transform classes using __call__ for transforms.Compose",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-076",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "In semantic segmentation or object detection, both the input image AND the pixel-wise segmentation mask "
            "(or bounding boxes) must undergo the exact same random spatial crop and horizontal flip. Why does passing "
            "the same `transforms.Compose([transforms.RandomCrop(128), transforms.RandomHorizontalFlip(p=0.5)])` "
            "separately to `img = tf(img)` and `mask = tf(mask)` fail?"
        ),
        "code": (
            "spatial_tf = transforms.Compose([\n"
            "    transforms.RandomCrop((128, 128)),\n"
            "    transforms.RandomHorizontalFlip(p=0.5)\n"
            "])\n"
            "# Inside SegmentationDataset.__getitem__:\n"
            "img = spatial_tf(img)\n"
            "mask = spatial_tf(mask)"
        ),
        "options": {
            "A": "Because each call to `spatial_tf(...)` draws independent random numbers, so `img` and `mask` receive different crop coordinates and may flip in opposite directions, misaligning the image and its ground-truth mask.",
            "B": "Because `RandomCrop` cannot be called more than once per epoch.",
            "C": "Because `RandomHorizontalFlip` converts segmentation mask integer class IDs into floating-point probabilities.",
            "D": "Because `transforms.Compose` caches the first image and returns `img` for both calls."
        },
        "correct": ["A"],
        "explanation": (
            "Calling `spatial_tf(img)` and then `spatial_tf(mask)` samples fresh random parameters on each call: `img` "
            "and `mask` get cropped at different $(i, j)$ locations and each has an independent 50% chance of being "
            "flipped, destroying pixel-level alignment! To apply identical random spatial parameters to both, either "
            "use `torchvision.transforms.v2` (passing `img, mask = spatial_tf(img, mask)` where `mask` is wrapped in "
            "`tv_tensors.Mask`) or use `transforms.RandomCrop.get_params(img, (128, 128))` with `transforms.functional.crop` / `hflip`."
        ),
        "option_explanations": {
            "A": "Correct. Separate calls draw independent random crop coordinates and flip decisions, desynchronizing `img` and `mask`.",
            "B": "Incorrect. `RandomCrop` can be called any number of times.",
            "C": "Incorrect. `RandomHorizontalFlip` flips spatial columns without altering pixel values or dtypes.",
            "D": "Incorrect. `transforms.Compose` is stateless and does not cache previous inputs."
        },
        "competency": "Synchronize random geometric transforms across images and target masks/boxes",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-077",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Easy",
        "multi_select": False,
        "stem": (
            "Suppose a dataset has $N = 1,001$ samples and you call `torch.utils.data.random_split(dataset, [0.8, 0.2])` "
            "using fractional proportions. How does PyTorch handle fractional lengths when $0.8 \\times 1001 = 800.8$ "
            "and $0.2 \\times 1001 = 200.2$?"
        ),
        "code": (
            "from torch.utils.data import random_split\n\n"
            "# len(dataset) == 1001\n"
            "train_sub, val_sub = random_split(dataset, [0.8, 0.2])\n"
            "print(len(train_sub), len(val_sub))"
        ),
        "options": {
            "A": "It raises a `ValueError` because `1001` is not evenly divisible by `5`.",
            "B": "It floors each length (`800` and `200`) and distributes any remaining samples (`1` sample) so that `len(train_sub) + len(val_sub) == 1001` (no samples are lost).",
            "C": "It drops the remainder sample, returning subsets of lengths `800` and `200` (sum `= 1000`).",
            "D": "It rounds both up (`801` and `201`) and duplicates one sample."
        },
        "correct": ["B"],
        "explanation": (
            "When fractional proportions summing to `1.0` are passed to `random_split`, PyTorch computes "
            "`math.floor(frac * len(dataset))` for each split and then distributes the leftover remainder "
            "`len(dataset) - sum(subset_lengths)` across the splits (via largest fractional remainder / round-robin) "
            "so that the integer subset lengths sum to `len(dataset)` (`801` and `200`, summing to `1001`)."
        ),
        "option_explanations": {
            "A": "Incorrect. Fractional `random_split` handles arbitrary dataset sizes without requiring exact divisibility.",
            "B": "Correct. PyTorch guarantees that the resulting integer subset lengths sum to `len(dataset)` (`1001`) with no dropped or duplicated samples.",
            "C": "Incorrect. `random_split` never drops samples from the dataset.",
            "D": "Incorrect. `random_split` partitions a permutation of `range(len(dataset))` and never duplicates indices."
        },
        "competency": "Use fractional proportions in torch.utils.data.random_split on arbitrary dataset sizes",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-078",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "What happens if you pass integer split lengths to `torch.utils.data.random_split(dataset, [700, 200])` "
            "when `len(dataset)` is `1,000` (so the sum of lengths `900` does NOT equal `1,000`)?"
        ),
        "code": (
            "from torch.utils.data import random_split\n\n"
            "# len(dataset) == 1000\n"
            "train_sub, val_sub = random_split(dataset, [700, 200])"
        ),
        "options": {
            "A": "It returns two subsets of size `700` and `200` and silently discards the remaining `100` samples.",
            "B": "It returns three subsets of size `700`, `200`, and `100`.",
            "C": "It raises a `ValueError: Sum of input lengths does not equal the length of the input dataset!`.",
            "D": "It scales `[700, 200]` proportionally to `[778, 222]`."
        },
        "correct": ["C"],
        "explanation": (
            "When integer lengths are passed to `random_split(dataset, lengths)`, PyTorch strictly verifies that "
            "`sum(lengths) == len(dataset)`. Because `700 + 200 = 900 != 1000`, it immediately raises "
            "`ValueError: Sum of input lengths does not equal the length of the input dataset!`."
        ),
        "option_explanations": {
            "A": "Incorrect. `random_split` requires integer lengths to partition the entire dataset and does not silently discard samples.",
            "B": "Incorrect. `random_split` only returns as many `Subset` objects as elements in `lengths`.",
            "C": "Correct. Integer split lengths must sum exactly to `len(dataset)`, or a `ValueError` is raised.",
            "D": "Incorrect. Integer lengths are not rescaled; only floats in `[0.0, 1.0]` summing to `1.0` are treated as proportions."
        },
        "competency": "Diagnose ValueError when integer split lengths in random_split do not sum to len(dataset)",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-079",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Medium",
        "multi_select": False,
        "stem": (
            "You are fine-tuning a model pre-trained on ImageNet (such as `torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT)`). "
            "How should your input images be normalized in the preprocessing transform pipeline?"
        ),
        "code": (
            "from torchvision.models import resnet50, ResNet50_Weights\n\n"
            "weights = ResNet50_Weights.DEFAULT\n"
            "preprocess = weights.transforms()"
        ),
        "options": {
            "A": "Normalize using the pre-trained model's ImageNet `mean=[0.485, 0.456, 0.406]` and `std=[0.229, 0.224, 0.225]` (or call `weights.transforms()` directly) so the input activation distribution matches what the pre-trained convolutional filters expect.",
            "B": "Do not normalize the images at all; leave pixel values in `[0, 255]`.",
            "C": "Normalize using `mean=[0.0, 0.0, 0.0]` and `std=[1.0, 1.0, 1.0]`.",
            "D": "Normalize each individual test image by its own single-image mean and std."
        },
        "correct": ["A"],
        "explanation": (
            "Pre-trained `torchvision.models` weights were trained on inputs normalized with ImageNet channel statistics "
            "(`mean=[0.485, 0.456, 0.406]`, `std=[0.229, 0.224, 0.225]`). Using `weights.transforms()` (or explicitly "
            "applying those exact `mean` and `std` values after scaling to `[0.0, 1.0]`) ensures the input distribution "
            "matches the pre-trained feature extractor's learned weights and BatchNorm running statistics."
        ),
        "option_explanations": {
            "A": "Correct. Pre-trained models expect inputs normalized with the same `mean` and `std` used during pre-training (accessible via `weights.transforms()`).",
            "B": "Incorrect. Passing `[0, 255]` values into a network trained on normalized `~[-2.1, 2.6]` inputs saturates activations and ruins transfer learning.",
            "C": "Incorrect. Identity normalization `(0, 1)` leaves inputs in `[0.0, 1.0]`, shifting the mean and variance away from the pre-trained filters.",
            "D": "Incorrect. Per-image normalization alters relative brightness/contrast across samples rather than matching the pre-trained dataset statistics."
        },
        "competency": "Match input normalization transforms to pre-trained model weight statistics",
        "source": "LFD2001 Ch. 4"
    },
    {
        "id": "PTCA-D-080",
        "domain": "Data Handling",
        "domain_code": "D",
        "subtopic": D3,
        "difficulty": "Hard",
        "multi_select": False,
        "stem": (
            "A web-scraped image dataset contains a small fraction (<0.1%) of corrupted JPEG files where `PIL.Image.open(path).convert('RGB')` "
            "raises `PIL.UnidentifiedImageError` or `OSError` inside `Dataset.__getitem__`. If you cannot pre-scan the "
            "entire multi-terabyte remote bucket beforehand, which strategy inside `__getitem__` or `collate_fn` safely "
            "prevents a single corrupted file from crashing a multi-day training run while maintaining valid tensor batches?"
        ),
        "code": (
            "class RobustWebDataset(Dataset):\n"
            "    def __init__(self, urls, transform=None):\n"
            "        self.urls = urls\n"
            "        self.transform = transform\n"
            "    def __len__(self):\n"
            "        return len(self.urls)\n"
            "    def __getitem__(self, idx):\n"
            "        # How can corrupted files be handled safely?"
        ),
        "options": {
            "A": "Catch `(OSError, SyntaxError)` inside `__getitem__`: either return `None` and filter out `None` entries in a custom `collate_fn` (`batch = [b for b in batch if b is not None]`, followed by `default_collate(batch)`), or retry with a valid replacement index.",
            "B": "Catch `OSError` inside `__getitem__` and return an empty tuple `()` while keeping the default `collate_fn`.",
            "C": "Catch `OSError` inside `__getitem__` and return a tensor of `float('nan')` values of shape `(3, 224, 224)`.",
            "D": "Set `drop_last=True` in `DataLoader`, which automatically catches `OSError` in `__getitem__`."
        },
        "correct": ["A"],
        "explanation": (
            "If `__getitem__` encounters a corrupted file, catching the I/O exception and either (1) returning `None` "
            "paired with a custom `collate_fn` that filters out `None` samples before calling `default_collate`, or "
            "(2) sampling a fallback valid index `(idx + 1) % len(self)` (with a bounded retry count), prevents the "
            "worker from raising an unhandled exception while ensuring `DataLoader` yields a valid tensor batch."
        ),
        "option_explanations": {
            "A": "Correct. Catching the I/O error in `__getitem__` and either filtering `None` in a custom `collate_fn` or substituting a valid sample keeps training running cleanly.",
            "B": "Incorrect. Returning `()` for one sample while other samples return 2-tuples `(img, label)` causes `default_collate` to fail when transposing/stacking.",
            "C": "Incorrect. Returning a tensor of `NaN`s will corrupt the loss, gradients, and model weights on the very next optimizer step.",
            "D": "Incorrect. `drop_last=True` only drops the final incomplete batch of an epoch; it does not catch exceptions raised inside `__getitem__`."
        },
        "competency": "Handle corrupted samples gracefully using custom Dataset exception handling and collate_fn filtering",
        "source": "LFD2001 Ch. 3 & Ch. 4"
    },
])


def balance_options(questions):
    """Deterministically rotate option letters so A, B, C, D are evenly distributed."""
    letters = ["A", "B", "C", "D"]
    for idx, q in enumerate(questions):
        if not q["multi_select"]:
            target_letter = letters[idx % 4]
            curr_letter = q["correct"][0]
            if curr_letter != target_letter:
                # Swap curr_letter and target_letter in options and option_explanations
                opts = dict(q["options"])
                opt_exps = dict(q["option_explanations"])
                opts[curr_letter], opts[target_letter] = opts[target_letter], opts[curr_letter]
                opt_exps[curr_letter], opt_exps[target_letter] = opt_exps[target_letter], opt_exps[curr_letter]
                q["options"] = {k: opts[k] for k in letters}
                q["option_explanations"] = {k: opt_exps[k] for k in letters}
                q["correct"] = [target_letter]


def main():
    assert len(QUESTIONS) == 80, f"Expected 80 questions, got {len(QUESTIONS)}"
    balance_options(QUESTIONS)
    seen_ids = set()
    seen_stems = set()
    code_count = 0
    subtopic_counts = {D1: 0, D2: 0, D3: 0}

    required_keys = {
        "id",
        "domain",
        "domain_code",
        "subtopic",
        "difficulty",
        "multi_select",
        "stem",
        "code",
        "options",
        "correct",
        "explanation",
        "option_explanations",
        "competency",
        "source",
    }

    for i, q in enumerate(QUESTIONS, start=1):
        expected_id = f"PTCA-D-{i:03d}"
        assert q["id"] == expected_id, f"ID mismatch at {i}: {q['id']} != {expected_id}"
        assert set(q.keys()) == required_keys, f"Keys mismatch in {q['id']}: {set(q.keys())}"
        assert q["domain"] == "Data Handling"
        assert q["domain_code"] == "D"
        assert q["subtopic"] in subtopic_counts, f"Invalid subtopic in {q['id']}: {q['subtopic']}"
        subtopic_counts[q["subtopic"]] += 1
        assert q["difficulty"] in ("Easy", "Medium", "Hard")
        assert isinstance(q["multi_select"], bool)
        assert isinstance(q["stem"], str) and len(q["stem"].strip()) > 20
        assert q["stem"] not in seen_stems, f"Duplicate stem in {q['id']}"
        seen_stems.add(q["stem"])
        seen_ids.add(q["id"])
        assert isinstance(q["code"], str)
        if q["code"].strip():
            code_count += 1
        assert set(q["options"].keys()) == {"A", "B", "C", "D"}
        assert set(q["option_explanations"].keys()) == {"A", "B", "C", "D"}
        for k in ("A", "B", "C", "D"):
            assert len(q["options"][k].strip()) > 0
            assert len(q["option_explanations"][k].strip()) > 0
            if k in q["correct"]:
                assert q["option_explanations"][k].startswith("Correct."), (
                    f"{q['id']} option {k} is in correct={q['correct']} but explanation does not start with 'Correct.'"
                )
            else:
                assert q["option_explanations"][k].startswith("Incorrect."), (
                    f"{q['id']} option {k} is not in correct={q['correct']} but explanation does not start with 'Incorrect.'"
                )
        assert isinstance(q["correct"], list) and len(q["correct"]) >= 1
        if q["multi_select"]:
            assert len(q["correct"]) >= 2
        else:
            assert len(q["correct"]) == 1
        for c in q["correct"]:
            assert c in ("A", "B", "C", "D")
        assert len(q["explanation"].strip()) > 20
        assert len(q["competency"].strip()) > 10
        assert len(q["source"].strip()) > 5

    assert subtopic_counts[D1] == 22, f"Expected 22 D1, got {subtopic_counts[D1]}"
    assert subtopic_counts[D2] == 28, f"Expected 28 D2, got {subtopic_counts[D2]}"
    assert subtopic_counts[D3] == 30, f"Expected 30 D3, got {subtopic_counts[D3]}"
    assert code_count >= 52, f"Expected at least 65% (52) questions with code, got {code_count}"

    out_path = Path(__file__).resolve().parent / "domain_d.json"
    out_path.write_text(json.dumps(QUESTIONS, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Successfully generated {len(QUESTIONS)} questions to {out_path}")
    print(f"Subtopic distribution: {subtopic_counts}")
    print(f"Questions with code snippets: {code_count}/{len(QUESTIONS)} ({code_count / len(QUESTIONS) * 100:.1f}%)")


if __name__ == "__main__":
    main()
