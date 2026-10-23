import json
import os

questions = []

def add_q(q_id, subtopic, difficulty, multi_select, stem, code, options, correct, explanation, option_explanations, competency, source):
    questions.append({
        "id": q_id,
        "domain": "PyTorch Fundamentals",
        "domain_code": "A",
        "subtopic": subtopic,
        "difficulty": difficulty,
        "multi_select": multi_select,
        "stem": stem,
        "code": code,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "option_explanations": option_explanations,
        "competency": competency,
        "source": source
    })

A1 = "A1: Core Concepts & Tensor Creation"

add_q(
    "PTCA-F-001", A1, "Easy", False,
    "In the context of artificial intelligence and the PyTorch curriculum, what structurally distinguishes Deep Learning (DL) from traditional Machine Learning (ML)?",
    "",
    {
        "A": "Deep Learning requires manual feature engineering before passing inputs to a model, whereas traditional ML extracts features automatically.",
        "B": "Deep Learning is a subset of Machine Learning that uses neural networks with multiple hidden layers (typically more than two) to learn representations from large datasets.",
        "C": "Deep Learning operates exclusively on unlabeled data, whereas Machine Learning operates exclusively on labeled data.",
        "D": "Machine Learning is a specialized subset of Deep Learning designed for small tabular datasets."
    },
    ["B"],
    "Deep Learning is a subset of Machine Learning characterized by neural networks with multiple hidden layers (usually more than two) that learn hierarchical representations from large amounts of data.",
    {
        "A": "Incorrect. Deep learning automates feature representation learning across multiple layers, reducing manual feature engineering.",
        "B": "Correct. DL is a subset of ML that utilizes multi-layer neural networks (typically >2 hidden layers) to learn from large data.",
        "C": "Incorrect. Both ML and DL can be applied to supervised (labeled), unsupervised (unlabeled), and reinforcement learning paradigms.",
        "D": "Incorrect. The hierarchy is reversed: Deep Learning is a subset of Machine Learning, which is a subset of AI."
    },
    "Understand the relationship between AI, Machine Learning, and Deep Learning",
    "modules/module_1_pytorch_overview/1_overview-ml-dl-pytorch.ipynb"
)

add_q(
    "PTCA-F-002", A1, "Easy", False,
    "A data science team wants to detect anomalous network traffic packets and group similar traffic patterns together, but they have no prior ground-truth labels for normal vs. anomalous packets. Which machine learning paradigm best describes this task?",
    "",
    {
        "A": "Supervised learning",
        "B": "Unsupervised learning",
        "C": "Reinforcement learning",
        "D": "Curriculum learning with teacher forcing"
    },
    ["B"],
    "Unsupervised learning discovers hidden patterns, clusters, and outliers/anomalies directly from input features without requiring labeled target data.",
    {
        "A": "Incorrect. Supervised learning requires labeled examples pairing input features with known target outputs.",
        "B": "Correct. Unsupervised learning finds commonalities, clusters, and anomalies in unlabeled data.",
        "C": "Incorrect. Reinforcement learning trains an agent via environment interactions using reward and punishment signals.",
        "D": "Incorrect. Teacher forcing is a sequence-to-sequence supervised training technique requiring ground-truth target sequences."
    },
    "Distinguish supervised, unsupervised, and reinforcement learning paradigms",
    "modules/module_1_pytorch_overview/1_overview-ml-dl-pytorch.ipynb"
)

add_q(
    "PTCA-F-003", A1, "Easy", False,
    "Which learning paradigm trains an autonomous agent to determine optimal behavior in an environment by rewarding desired actions and penalizing undesired ones over time?",
    "",
    {
        "A": "Supervised classification",
        "B": "Unsupervised clustering",
        "C": "Reinforcement learning",
        "D": "Semi-supervised dimensionality reduction"
    },
    ["C"],
    "Reinforcement learning optimizes sequential decision-making by rewarding positive behavior and punishing negative behavior within an environment.",
    {
        "A": "Incorrect. Supervised classification learns a mapping from features to discrete ground-truth class labels.",
        "B": "Incorrect. Unsupervised clustering groups unlabeled data points by feature similarity without reward feedback.",
        "C": "Correct. Reinforcement learning uses reward and penalty signals to learn optimal policy behavior in an environment.",
        "D": "Incorrect. Dimensionality reduction compresses feature representations rather than learning action policies via rewards."
    },
    "Identify reinforcement learning characteristics",
    "modules/module_1_pytorch_overview/1_overview-ml-dl-pytorch.ipynb"
)

add_q(
    "PTCA-F-004", A1, "Medium", False,
    "Why is PyTorch's default execution model ('eager mode') particularly advantageous during model prototyping and debugging compared to static graph execution?",
    "",
    {
        "A": "Eager mode pre-compiles the entire Python file into a C++ binary before executing the first line of code.",
        "B": "Operations are evaluated immediately as they are encountered in Python, allowing standard Python control flow, print statements, and interactive debuggers (`pdb`) to inspect intermediate tensors on the fly.",
        "C": "Eager mode automatically disables gradient tracking (`requires_grad=False`) for all `torch.nn.Module` parameters to save memory.",
        "D": "Eager mode eliminates the need for GPU device placement by executing all tensor operations on CPU and GPU simultaneously."
    },
    ["B"],
    "In eager mode (define-by-run), tensor operations execute immediately as Python statements run, enabling dynamic control flow and inspection with standard Python debugging tools, whereas graph/compiler mode focuses on whole-graph production optimizations.",
    {
        "A": "Incorrect. Pre-compiling a static graph before execution describes ahead-of-time graph compilation, not eager execution.",
        "B": "Correct. Eager mode evaluates operations immediately and builds the dynamic computation graph on the fly, making prototyping and debugging Pythonic.",
        "C": "Incorrect. `nn.Module` parameters have `requires_grad=True` by default in eager mode so autograd can record operations.",
        "D": "Incorrect. Tensors still reside on a specific device (`cpu`, `cuda`, etc.) and must be explicitly placed or moved."
    },
    "Contrast PyTorch eager execution mode with compiled graph mode",
    "modules/module_1_pytorch_overview/1_overview-ml-dl-pytorch.ipynb"
)

add_q(
    "PTCA-F-005", A1, "Easy", False,
    "According to PyTorch installation guidelines, when should a user build and install PyTorch from source code rather than installing a pre-built binary via `pip` or `conda`?",
    "",
    {
        "A": "Whenever GPU (CUDA) acceleration is required, because pre-built binaries only support CPU execution.",
        "B": "Whenever installing PyTorch on macOS or Windows, as pre-built wheels are only published for Linux.",
        "C": "When testing bleeding-edge upstream features, compiling for custom/unsupported build configurations, or actively contributing to PyTorch core development.",
        "D": "Whenever `torch.utils.data.DataLoader` multiprocessing is needed in a training script."
    },
    ["C"],
    "Pre-built binaries via package managers provide the best experience for most users across Linux, macOS, and Windows (including GPU support). Building from source is intended for bleeding-edge testing or contributing to PyTorch core.",
    {
        "A": "Incorrect. Pre-built binaries include full support for CUDA/ROCm acceleration selectable via the PyTorch getting-started matrix.",
        "B": "Incorrect. Pre-built binaries are officially provided for Linux, macOS, and Windows.",
        "C": "Correct. Installing from source is needed when working with bleeding-edge commits or developing PyTorch core.",
        "D": "Incorrect. `DataLoader` multiprocessing works out of the box with standard pre-built binary installations."
    },
    "Determine when to use pre-built binaries versus source installation",
    "modules/module_1_pytorch_overview/2_pytorch_installation.ipynb"
)

add_q(
    "PTCA-F-006", A1, "Easy", False,
    "Which Python expression inspects the installed PyTorch release version string (including any build suffix such as `+cu121` or `+cpu`), and how can CUDA runtime availability be verified?",
    "import torch\n# Inspect version and check if CUDA is usable",
    {
        "A": "torch.version() and torch.has_cuda()",
        "B": "torch.__version__ and torch.cuda.is_available()",
        "C": "torch.get_version() and torch.device.is_cuda()",
        "D": "torch.__release__ and torch.cuda.enabled()"
    },
    ["B"],
    "`torch.__version__` returns the installed version string (e.g., `'2.4.0+cu121'`), and `torch.cuda.is_available()` returns a boolean indicating whether a CUDA-capable GPU and runtime are accessible.",
    {
        "A": "Incorrect. `torch.version` is a module (not a callable function), and `torch.has_cuda` is not the standard availability check.",
        "B": "Correct. `torch.__version__` holds the version string attribute, and `torch.cuda.is_available()` checks GPU readiness.",
        "C": "Incorrect. Neither `torch.get_version()` nor `torch.device.is_cuda()` exists in PyTorch.",
        "D": "Incorrect. `torch.__release__` and `torch.cuda.enabled()` are not valid PyTorch APIs."
    },
    "Verify PyTorch installation version and hardware availability",
    "modules/module_1_pytorch_overview/2_pytorch_installation.ipynb"
)

add_q(
    "PTCA-F-007", A1, "Medium", False,
    "What is the output of the following code comparing `torch.tensor()`, `torch.as_tensor()`, and `torch.from_numpy()` when the underlying NumPy array is modified in-place?",
    "import numpy as np\nimport torch\n\narr = np.array([10, 20, 30])\nt_copy = torch.tensor(arr)\nt_view1 = torch.as_tensor(arr)\nt_view2 = torch.from_numpy(arr)\n\narr[0] = 99\nprint(int(t_copy[0]), int(t_view1[0]), int(t_view2[0]))",
    {
        "A": "99 99 99",
        "B": "10 99 99",
        "C": "10 10 99",
        "D": "10 10 10"
    },
    ["B"],
    "`torch.tensor()` always copies the input data into new memory. Both `torch.as_tensor()` (when given a CPU NumPy array with compatible dtype/device) and `torch.from_numpy()` share the underlying memory buffer with the NumPy array, so mutating `arr[0] = 99` updates `t_view1` and `t_view2` while `t_copy` stays `10`.",
    {
        "A": "Incorrect. `torch.tensor()` always makes an independent copy of the data, so `t_copy[0]` remains `10`.",
        "B": "Correct. `torch.tensor()` copies (`10`), while `torch.as_tensor()` and `torch.from_numpy()` share memory with `arr` (`99`).",
        "C": "Incorrect. `torch.as_tensor()` avoids copying whenever the source is already a NumPy array with matching dtype and CPU device.",
        "D": "Incorrect. `torch.from_numpy()` and `torch.as_tensor()` create zero-copy views over the NumPy array's buffer."
    },
    "Distinguish memory sharing behavior across torch.tensor, torch.as_tensor, and torch.from_numpy",
    " PyTorch Docs: Tensor Creation Ops (torch.tensor, torch.as_tensor, torch.from_numpy)"
)

add_q(
    "PTCA-F-008", A1, "Medium", False,
    "A developer passes a standard Python list `[1.0, 2.0, 3.0]` to both `torch.as_tensor()` and `torch.from_numpy()`. What happens in each call?",
    "import torch\n\ndata = [1.0, 2.0, 3.0]\na = torch.as_tensor(data)\nb = torch.from_numpy(data)",
    {
        "A": "Both calls succeed and share memory directly with the Python list.",
        "B": "`torch.as_tensor(data)` succeeds by converting the list into a new tensor, whereas `torch.from_numpy(data)` raises a `TypeError` because it strictly requires a `numpy.ndarray`.",
        "C": "Both calls raise a `TypeError` because neither accepts native Python sequences.",
        "D": "`torch.from_numpy(data)` automatically calls `np.asarray(data)` first, whereas `torch.as_tensor(data)` raises a `ValueError`."
    },
    ["B"],
    "`torch.as_tensor()` accepts any array-like object (lists, tuples, NumPy arrays, existing tensors), copying only when necessary. `torch.from_numpy()` strictly requires a `numpy.ndarray` and raises `TypeError: expected np.ndarray (got list)`.",
    {
        "A": "Incorrect. Python lists do not expose a contiguous C buffer for tensor storage, and `from_numpy` rejects lists.",
        "B": "Correct. `torch.as_tensor` converts sequences into a tensor, while `torch.from_numpy` only accepts `numpy.ndarray` instances.",
        "C": "Incorrect. `torch.as_tensor` accepts Python lists, tuples, scalars, and NumPy arrays.",
        "D": "Incorrect. `torch.from_numpy` does not implicitly convert lists to NumPy arrays."
    },
    "Understand input constraints of torch.as_tensor versus torch.from_numpy",
    "PyTorch Docs: torch.as_tensor and torch.from_numpy"
)

add_q(
    "PTCA-F-009", A1, "Easy", False,
    "What is the difference between `torch.zeros(2, 3)` and `torch.empty(2, 3)`?",
    "import torch\nz = torch.zeros(2, 3)\ne = torch.empty(2, 3)",
    {
        "A": "`torch.empty(2, 3)` creates a tensor with `0` elements of shape `(0,)`, while `torch.zeros(2, 3)` allocates 6 zeros.",
        "B": "`torch.zeros(2, 3)` initializes all 6 elements to `0.0`, while `torch.empty(2, 3)` allocates memory for 6 elements without initializing them (containing whatever arbitrary bytes were in memory).",
        "C": "`torch.empty(2, 3)` initializes all elements to `float('nan')`, while `torch.zeros(2, 3)` initializes them to `0`.",
        "D": "`torch.zeros(2, 3)` creates a `float32` tensor, while `torch.empty(2, 3)` creates a `bool` tensor."
    },
    ["B"],
    "`torch.empty(2, 3)` allocates a `(2, 3)` tensor buffer without zeroing or setting its values, so it contains arbitrary uninitialized memory values. `torch.zeros(2, 3)` explicitly sets every element to `0.0`.",
    {
        "A": "Incorrect. Both `z` and `e` have shape `torch.Size([2, 3])` and `numel() == 6`.",
        "B": "Correct. `torch.empty` skips memory initialization for performance when the buffer will be immediately overwritten.",
        "C": "Incorrect. `torch.empty` does not write `NaN`s; it leaves existing memory bytes untouched (which may include zeros, garbage floats, etc.).",
        "D": "Incorrect. Both default to `torch.get_default_dtype()`, which is `torch.float32`."
    },
    "Differentiate initialized factory methods (zeros/ones) from uninitialized allocation (empty)",
    "modules/module_2_tensors/1_tensor_basic.ipynb"
)

add_q(
    "PTCA-F-010", A1, "Easy", False,
    "Which function call creates a 2D tensor of shape `(3, 4)` where every element is initialized to the integer `-1` (`torch.int64`)?",
    "import torch\n# Create a (3, 4) tensor filled with -1",
    {
        "A": "torch.full(3, 4, fill_value=-1)",
        "B": "torch.full((3, 4), -1, dtype=torch.long)",
        "C": "torch.ones((3, 4), value=-1)",
        "D": "torch.empty((3, 4), fill=-1)"
    },
    ["B"],
    "`torch.full(size, fill_value, ...)` requires `size` as a tuple or list of integers `(3, 4)` as its first argument, followed by `fill_value=-1`.",
    {
        "A": "Incorrect. Passing `3, 4` positionally passes `3` as `size` and `4` as `fill_value`, causing a `TypeError`.",
        "B": "Correct. `torch.full((3, 4), -1, dtype=torch.long)` creates a `(3, 4)` tensor of `int64` values all equal to `-1`.",
        "C": "Incorrect. `torch.ones()` does not accept a `value` keyword argument.",
        "D": "Incorrect. `torch.empty()` does not accept a `fill` keyword argument."
    },
    "Use torch.full with proper size tuple and fill_value signature",
    "PyTorch Docs: torch.full"
)

add_q(
    "PTCA-F-011", A1, "Medium", False,
    "What is the output of the following code using `torch.eye` and `torch.diag`?",
    "import torch\n\nI = torch.eye(3, 4)\nv = torch.tensor([2, 5, 8])\nD = torch.diag(v, diagonal=1)\nprint(I.shape, D.shape, int(D[0, 1]))",
    {
        "A": "torch.Size([3, 4]) torch.Size([3, 3]) 2",
        "B": "torch.Size([3, 4]) torch.Size([4, 4]) 2",
        "C": "torch.Size([3, 3]) torch.Size([4, 4]) 5",
        "D": "torch.Size([3, 4]) torch.Size([4, 4]) 0"
    },
    ["B"],
    "`torch.eye(n, m)` creates an `(n, m)` rectangular matrix with ones on the main diagonal (`(3, 4)`). When given a 1D vector of length `3` and `diagonal=1` (one superdiagonal above the main diagonal), `torch.diag` constructs a `(3 + 1, 3 + 1) = (4, 4)` matrix where `D[0, 1]` is the first element of `v` (`2`).",
    {
        "A": "Incorrect. Shifting a 3-element vector to `diagonal=1` expands the square matrix size by 1 in each dimension to `(4, 4)`.",
        "B": "Correct. `I` has shape `(3, 4)`, `D` has shape `(4, 4)`, and the superdiagonal starts at `[0, 1]` with value `2`.",
        "C": "Incorrect. `torch.eye(3, 4)` produces a `(3, 4)` tensor, and `D[0, 1]` is the first element of `v`, which is `2`.",
        "D": "Incorrect. `D[0, 1]` lies on the first superdiagonal (`diagonal=1`), so it equals `v[0] = 2`, not `0`."
    },
    "Construct identity and diagonal matrices using torch.eye and torch.diag",
    "PyTorch Docs: torch.eye and torch.diag"
)

add_q(
    "PTCA-F-012", A1, "Medium", False,
    "What happens when a 2D matrix is passed to `torch.diag()` instead of a 1D vector?",
    "import torch\n\nM = torch.arange(1, 10).reshape(3, 3)\n# M is [[1, 2, 3],\n#       [4, 5, 6],\n#       [7, 8, 9]]\nout = torch.diag(M, diagonal=-1)\nprint(out)",
    {
        "A": "It raises a `RuntimeError` because `torch.diag` only accepts 1D tensors.",
        "B": "It returns `tensor([4, 8])`, extracting the first subdiagonal below the main diagonal as a 1D tensor.",
        "C": "It returns a `(3, 3)` matrix with `[4, 8]` on the subdiagonal and zeros everywhere else.",
        "D": "It returns `tensor([2, 6])`, extracting the first superdiagonal above the main diagonal."
    },
    ["B"],
    "`torch.diag()` is polymorphic: if the input is a 1D vector, it constructs a 2D diagonal matrix; if the input is a 2D matrix, it extracts the specified diagonal (`diagonal=-1` is one below the main diagonal: elements `[1, 0]=4` and `[2, 1]=8`) as a 1D tensor.",
    {
        "A": "Incorrect. `torch.diag` accepts both 1D and 2D tensors.",
        "B": "Correct. For a 2D input and `diagonal=-1`, `torch.diag` extracts the subdiagonal `tensor([4, 8])`.",
        "C": "Incorrect. Extracting and zeroing out off-diagonal elements while keeping a 2D matrix requires `torch.diag(torch.diag(M))` or `torch.tril`/`torch.triu`.",
        "D": "Incorrect. `tensor([2, 6])` corresponds to `diagonal=1` (above the main diagonal), not `diagonal=-1`."
    },
    "Extract matrix diagonals using torch.diag on 2D inputs",
    "PyTorch Docs: torch.diag"
)

add_q(
    "PTCA-F-013", A1, "Medium", False,
    "Compare `torch.arange`, `torch.linspace`, and `torch.logspace` in the code snippet below. What is printed?",
    "import torch\n\na = torch.arange(0, 10, 2)\nl = torch.linspace(0, 10, steps=5)\ng = torch.logspace(start=0, end=2, steps=3, base=10.0)\nprint(len(a), float(a[-1]), float(l[-1]), float(g[-1]))",
    {
        "A": "5 8.0 10.0 100.0",
        "B": "6 10.0 10.0 100.0",
        "C": "5 8.0 8.0 2.0",
        "D": "5 10.0 10.0 10.0"
    },
    ["A"],
    "`torch.arange(start, end, step)` generates values in the half-open interval `[start, end)`, yielding `[0, 2, 4, 6, 8]` (5 elements, last is `8`). `torch.linspace(start, end, steps)` and `torch.logspace(start, end, steps, base)` both include the `end` boundary: `linspace(0, 10, 5)` ends at `10.0`, and `logspace(0, 2, 3, base=10)` generates `[10^0, 10^1, 10^2] = [1.0, 10.0, 100.0]`.",
    {
        "A": "Correct. `arange` excludes `end` (`len=5`, last=`8.0`), `linspace` includes `end` (`10.0`), and `logspace` computes `base**end` (`10.0**2 = 100.0`).",
        "B": "Incorrect. `torch.arange(0, 10, 2)` is exclusive of `10`, so it has 5 elements ending at `8`.",
        "C": "Incorrect. `torch.linspace` includes the endpoint `10.0`, and `torch.logspace` raises `base` to the powers from `start` to `end`.",
        "D": "Incorrect. `a[-1]` is `8.0` and `g[-1]` is `10**2 = 100.0`."
    },
    "Contrast endpoint inclusion and scaling in arange, linspace, and logspace",
    "PyTorch Docs: torch.arange, torch.linspace, torch.logspace"
)

add_q(
    "PTCA-F-014", A1, "Easy", False,
    "What are the default data types (`dtype`) of the tensors created by `torch.arange(5)` versus `torch.linspace(0, 4, steps=5)`?",
    "import torch\na = torch.arange(5)\nb = torch.linspace(0, 4, steps=5)\nprint(a.dtype, b.dtype)",
    {
        "A": "torch.int64 torch.float32",
        "B": "torch.float32 torch.float32",
        "C": "torch.int32 torch.float64",
        "D": "torch.int64 torch.int64"
    },
    ["A"],
    "When given integer arguments, `torch.arange` infers `torch.int64` (`torch.long`), whereas `torch.linspace` always defaults to the global default floating-point dtype (`torch.float32`) even when `start` and `end` are integers.",
    {
        "A": "Correct. `torch.arange(5)` produces `torch.int64`, while `torch.linspace` produces `torch.float32`.",
        "B": "Incorrect. `torch.arange` with integer arguments produces `torch.int64` unless a float argument or `dtype=torch.float32` is passed.",
        "C": "Incorrect. PyTorch's default integer type is 64-bit (`int64`) and default float type is 32-bit (`float32`).",
        "D": "Incorrect. `torch.linspace` computes evenly spaced real intervals and defaults to `torch.float32`."
    },
    "Identify default dtypes of range-generating factory functions",
    "PyTorch Docs: torch.arange and torch.linspace"
)

add_q(
    "PTCA-F-015", A1, "Easy", False,
    "Which statement accurately contrasts `torch.rand(1000)` and `torch.randn(1000)`?",
    "import torch\nu = torch.rand(1000)\nn = torch.randn(1000)",
    {
        "A": "`torch.rand` samples from a continuous uniform distribution over $[0, 1)$, while `torch.randn` samples from a standard normal (Gaussian) distribution with mean $0$ and variance $1$.",
        "B": "`torch.rand` samples random integers, while `torch.randn` samples random floating-point numbers.",
        "C": "`torch.rand` samples from $[-1, 1]$, while `torch.randn` samples from $[0, 1)$.",
        "D": "`torch.rand` is deterministic without a seed, while `torch.randn` uses hardware entropy."
    },
    ["A"],
    "`torch.rand` draws samples from the uniform distribution $[0, 1)$, whereas `torch.randn` draws samples from the standard normal distribution $\\mathcal{N}(0, 1)$ (which can produce both positive and negative values unbounded in principle).",
    {
        "A": "Correct. `rand` is uniform on $[0, 1)$ and `randn` is standard normal $\\mathcal{N}(0, 1)$.",
        "B": "Incorrect. Both return floating-point tensors; random integers are generated with `torch.randint`.",
        "C": "Incorrect. Generating uniform values in $[-1, 1)$ requires scaling, e.g., `torch.rand(...) * 2 - 1` (as shown in Module 2).",
        "D": "Incorrect. Both use the same pseudo-random number generator controlled by `torch.manual_seed`."
    },
    "Distinguish uniform (torch.rand) and standard normal (torch.randn) random tensor creation",
    "modules/module_2_tensors/1_tensor_basic.ipynb"
)

add_q(
    "PTCA-F-016", A1, "Medium", False,
    "A developer wants to simulate rolling a fair 6-sided die (values `1, 2, 3, 4, 5, 6`) 100 times in a 1D tensor. Which `torch.randint` call is correct?",
    "import torch\n# Generate 100 random integers in {1, 2, 3, 4, 5, 6}",
    {
        "A": "torch.randint(1, 6, (100,))",
        "B": "torch.randint(1, 7, (100,))",
        "C": "torch.randint(1, 7, 100)",
        "D": "torch.randint(6, size=(100,))"
    },
    ["B"],
    "`torch.randint(low, high, size)` samples integers uniformly from the half-open interval `[low, high)` and requires `size` to be a tuple/list of dimensions `(100,)`. To include `6`, `high` must be `7`.",
    {
        "A": "Incorrect. Because `high` is exclusive, `torch.randint(1, 6, (100,))` only generates values in `{1, 2, 3, 4, 5}`.",
        "B": "Correct. `low=1, high=7` samples from `[1, 7)` = `{1, 2, 3, 4, 5, 6}`, and `(100,)` is a valid size tuple.",
        "C": "Incorrect. `size` in `torch.randint` must be a tuple of ints `(100,)`, not a bare integer `100` (which raises a `TypeError`).",
        "D": "Incorrect. When `low` is omitted, it defaults to `0`, so `torch.randint(6, size=(100,))` samples from `{0, 1, 2, 3, 4, 5}`."
    },
    "Use torch.randint with exclusive upper bound and tuple size argument",
    "PyTorch Docs: torch.randint"
)

add_q(
    "PTCA-F-017", A1, "Easy", False,
    "Which PyTorch function generates a 1D tensor containing a random permutation of the integers from `0` through `n - 1` (commonly used for shuffling dataset indices)?",
    "import torch\n# Create shuffled indices for a dataset of 50 samples",
    {
        "A": "torch.randperm(50)",
        "B": "torch.randint(0, 50, (50,))",
        "C": "torch.shuffle(torch.arange(50))",
        "D": "torch.permute(50)"
    },
    ["A"],
    "`torch.randperm(n)` returns a 1D tensor of `n` unique integers from `0` to `n - 1` in random order without replacement.",
    {
        "A": "Correct. `torch.randperm(50)` produces a random permutation of `0, 1, ..., 49`.",
        "B": "Incorrect. `torch.randint` samples with replacement, so duplicate indices will appear and some indices will be omitted.",
        "C": "Incorrect. There is no `torch.shuffle` function in PyTorch.",
        "D": "Incorrect. `torch.permute` rearranges dimensions of an existing tensor; it does not generate random permutations of integers."
    },
    "Generate random permutations without replacement using torch.randperm",
    "PyTorch Docs: torch.randperm"
)

add_q(
    "PTCA-F-018", A1, "Medium", False,
    "Given an existing tensor `x` on a specific device and dtype, what properties does `torch.zeros_like(x)` inherit by default, and how does it handle `requires_grad`?",
    "import torch\n\nx = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float64, requires_grad=True)\ny = torch.zeros_like(x)\nprint(y.shape, y.dtype, y.device, y.requires_grad)",
    {
        "A": "torch.Size([2, 2]) torch.float64 cpu True",
        "B": "torch.Size([2, 2]) torch.float64 cpu False",
        "C": "torch.Size([2, 2]) torch.float32 cpu False",
        "D": "torch.Size([2, 2]) torch.float64 cpu None"
    },
    ["B"],
    "`*_like` creation ops (`zeros_like`, `ones_like`, `empty_like`, `rand_like`, `randn_like`, `full_like`) preserve `x.shape`, `x.dtype`, `x.layout`, and `x.device` by default, but they do NOT copy `requires_grad=True` unless `requires_grad=True` is explicitly passed to `zeros_like`.",
    {
        "A": "Incorrect. `torch.zeros_like(x)` defaults to `requires_grad=False` even when `x.requires_grad` is `True`.",
        "B": "Correct. `y` matches `x`'s shape `(2, 2)`, dtype `torch.float64`, and device `cpu`, while `y.requires_grad` defaults to `False`.",
        "C": "Incorrect. `zeros_like` inherits `x.dtype` (`torch.float64`), rather than resetting to `torch.float32`.",
        "D": "Incorrect. `requires_grad` is a boolean attribute (`False`), never `None`."
    },
    "Understand attribute inheritance and requires_grad default in *_like factory functions",
    "PyTorch Docs: torch.zeros_like"
)

add_q(
    "PTCA-F-019", A1, "Medium", False,
    "What happens when you call `torch.randn_like(idx)` on an integer tensor `idx = torch.tensor([0, 1, 2], dtype=torch.int64)` without overriding the `dtype` argument?",
    "import torch\nidx = torch.tensor([0, 1, 2], dtype=torch.int64)\nout = torch.randn_like(idx)",
    {
        "A": "It automatically casts the output to `torch.float32` and returns 3 random normal floats.",
        "B": "It rounds the normal distribution samples to the nearest 64-bit integers.",
        "C": "It raises a `RuntimeError` (`\"normal_kernel_cpu\" not implemented for 'Long'`) because `randn_like` inherits `dtype=torch.int64`, and normal distribution sampling is only implemented for floating-point/complex dtypes.",
        "D": "It returns a tensor of zeros of type `torch.int64`."
    },
    ["C"],
    "Because `torch.randn_like(idx)` inherits `idx.dtype` (`torch.int64`), it attempts to run standard normal sampling on a `Long` tensor, which raises a `RuntimeError`. You must pass `dtype=torch.float32` explicitly: `torch.randn_like(idx, dtype=torch.float32)`.",
    {
        "A": "Incorrect. `randn_like` does not silently override the input tensor's `int64` dtype.",
        "B": "Incorrect. `randn` does not discretize continuous Gaussian samples into integers.",
        "C": "Correct. Inheriting `int64` causes `randn_like` to fail because continuous random sampling requires a floating-point or complex dtype.",
        "D": "Incorrect. It raises a `RuntimeError` rather than returning zeros."
    },
    "Avoid dtype mismatch errors when using rand_like/randn_like on integer tensors",
    "PyTorch Docs: torch.randn_like"
)

add_q(
    "PTCA-F-020", A1, "Easy", False,
    "What is the output of the following code inspecting a 0-dimensional (scalar) tensor?",
    "import torch\n\nt = torch.tensor(42)\nprint(t.ndim, t.shape, t.numel(), t.item())",
    {
        "A": "1 torch.Size([1]) 1 42",
        "B": "0 torch.Size([]) 1 42",
        "C": "0 torch.Size([]) 0 42",
        "D": "1 torch.Size([0]) 1 [42]"
    },
    ["B"],
    "Passing a Python scalar (`42`) to `torch.tensor()` creates a 0-dimensional (scalar) tensor: `t.ndim` is `0`, `t.shape` is `torch.Size([])`, `t.numel()` is `1` (an empty product of dimensions still holds 1 scalar value), and `t.item()` extracts the Python integer `42`.",
    {
        "A": "Incorrect. `torch.tensor(42)` is 0D (`ndim == 0`, `shape == torch.Size([])`), whereas `torch.tensor([42])` would be 1D (`ndim == 1`, `shape == torch.Size([1])`).",
        "B": "Correct. A 0D scalar tensor has `ndim=0`, `shape=torch.Size([])`, `numel()=1`, and `.item()=42`.",
        "C": "Incorrect. A 0D scalar tensor contains 1 element (`t.numel() == 1`), not 0 elements.",
        "D": "Incorrect. `torch.Size([0])` is an empty 1D tensor with 0 elements, not a 0D scalar tensor."
    },
    "Inspect dimensionality, shape, and element count of a 0D scalar tensor",
    "modules/module_2_tensors/1_tensor_basic.ipynb"
)

add_q(
    "PTCA-F-021", A1, "Easy", False,
    "Consider the four tensors defined below. Which option correctly classifies their ranks (number of dimensions) from `t1` through `t4`?",
    "import torch\n\nt1 = torch.tensor(3.14)\nt2 = torch.tensor([3.14])\nt3 = torch.tensor([[3.14]])\nt4 = torch.zeros(2, 1, 3)",
    {
        "A": "t1: 1D vector, t2: 1D vector, t3: 2D matrix, t4: 3D tensor",
        "B": "t1: 0D scalar, t2: 1D vector, t3: 2D matrix, t4: 3D tensor",
        "C": "t1: 0D scalar, t2: 0D scalar, t3: 1D vector, t4: 2D matrix",
        "D": "t1: Python float, t2: 1D vector, t3: 2D matrix, t4: 2D matrix"
    },
    ["B"],
    "`t1` has no brackets (`ndim=0`, scalar, shape `()`), `t2` has one level of brackets (`ndim=1`, vector, shape `(1,)`), `t3` has two nested levels (`ndim=2`, matrix, shape `(1, 1)`), and `t4` has three dimension sizes (`ndim=3`, 3D tensor, shape `(2, 1, 3)`).",
    {
        "A": "Incorrect. `t1 = torch.tensor(3.14)` has `ndim == 0` (0D scalar), not 1D.",
        "B": "Correct. The ranks are 0, 1, 2, and 3 respectively.",
        "C": "Incorrect. Wrapping a number in `[3.14]` adds a dimension (`ndim == 1`).",
        "D": "Incorrect. `t1` is a `torch.Tensor` of rank 0, and `t4` has 3 dimensions even though the middle dimension is size 1."
    },
    "Distinguish 0D scalars, 1D vectors, 2D matrices, and 3D tensors",
    "modules/module_2_tensors/1_tensor_basic.ipynb"
)

add_q(
    "PTCA-F-022", A1, "Medium", False,
    "In which of the following cases will calling `.item()` on a tensor `t` succeed WITHOUT raising a `RuntimeError`?",
    "import torch\n\na = torch.tensor(7.5)\nb = torch.tensor([[[7.5]]])\nc = torch.tensor([7.5, 8.5])\nd = torch.empty(0)",
    {
        "A": "Only on `a`, because `.item()` requires `t.ndim == 0`.",
        "B": "On both `a` and `b`, because `.item()` works on any tensor with `t.numel() == 1` regardless of the number of dimensions.",
        "C": "On `a`, `b`, and `c`, returning a tuple for `c`.",
        "D": "On `a`, `b`, and `d`, returning `None` for `d`."
    },
    ["B"],
    "`.item()` converts a single-element tensor (`t.numel() == 1`) into a standard Python scalar. It succeeds for both 0D scalar tensors (`a`, shape `()`) and higher-dimensional singleton tensors (`b`, shape `(1, 1, 1)`). Calling `.item()` when `numel() != 1` (such as `c` with 2 elements or `d` with 0 elements) raises `RuntimeError: a Tensor with X elements cannot be converted to Scalar`.",
    {
        "A": "Incorrect. `.item()` checks that `t.numel() == 1`, not that `t.ndim == 0`, so `b.item()` also returns `7.5`.",
        "B": "Correct. Both `a` and `b` have `numel() == 1`, so `.item()` returns the Python `float` `7.5` for both.",
        "C": "Incorrect. `c` has 2 elements and raises a `RuntimeError` when `.item()` is called.",
        "D": "Incorrect. `d` has 0 elements and also raises a `RuntimeError` when `.item()` is called."
    },
    "Extract Python scalars using .item() and understand its single-element requirement",
    "modules/module_2_tensors/1_tensor_basic.ipynb"
)

add_q(
    "PTCA-F-023", A1, "Easy", False,
    "What does `.tolist()` return when called on a 2D tensor versus a 0D scalar tensor?",
    "import torch\n\nm = torch.tensor([[1, 2], [3, 4]])\ns = torch.tensor(9)\nprint(type(m.tolist()), m.tolist(), type(s.tolist()), s.tolist())",
    {
        "A": "<class 'list'> [[1, 2], [3, 4]] <class 'int'> 9",
        "B": "<class 'list'> [1, 2, 3, 4] <class 'list'> [9]",
        "C": "<class 'numpy.ndarray'> [[1, 2], [3, 4]] <class 'int'> 9",
        "D": "<class 'list'> [[1, 2], [3, 4]] <class 'list'> [9]"
    },
    ["A"],
    "`tensor.tolist()` returns a nested Python `list` matching the tensor's dimensions for `ndim >= 1`, and returns a standard Python scalar (`int`, `float`, `bool`) when `ndim == 0` (behaving like `.item()` for 0D tensors).",
    {
        "A": "Correct. `m.tolist()` is a nested Python `list` `[[1, 2], [3, 4]]`, and for 0D `s`, `s.tolist()` returns the Python `int` `9`.",
        "B": "Incorrect. `.tolist()` preserves nested dimension structure rather than flattening, and returns a scalar for 0D tensors.",
        "C": "Incorrect. `.tolist()` returns native Python objects (`list` / scalars), not a `numpy.ndarray`.",
        "D": "Incorrect. For a 0-dimensional tensor `s`, `s.tolist()` returns `9` (`int`), not `[9]`."
    },
    "Convert tensors to nested Python lists or scalars with .tolist()",
    "PyTorch Docs: torch.Tensor.tolist"
)

add_q(
    "PTCA-F-024", A1, "Medium", False,
    "What is the output of the following code using `torch.manual_seed`?",
    "import torch\n\ntorch.manual_seed(123)\na = torch.rand(2)\nb = torch.rand(2)\n\ntorch.manual_seed(123)\nc = torch.rand(2)\n\nprint(torch.equal(a, b), torch.equal(a, c))",
    {
        "A": "True True",
        "B": "False True",
        "C": "False False",
        "D": "True False"
    },
    ["B"],
    "`torch.manual_seed(123)` resets the pseudo-random number generator (PRNG) state. The first call `a = torch.rand(2)` advances the PRNG state, so the subsequent call `b = torch.rand(2)` draws the next two numbers in the sequence (`a != b`). Resetting `torch.manual_seed(123)` restores the initial PRNG state, so `c = torch.rand(2)` produces the exact same values as `a` (`a == c`).",
    {
        "A": "Incorrect. Calling `torch.rand(2)` twice after a single seed advances the generator state, so `a` and `b` are different.",
        "B": "Correct. `a` and `b` are sequential draws (`False`), while re-seeding with `123` makes `c` identical to `a` (`True`).",
        "C": "Incorrect. Resetting `torch.manual_seed(123)` deterministically reproduces `a` in `c`.",
        "D": "Incorrect. `a` and `b` are not equal, while `a` and `c` are equal."
    },
    "Control reproducibility of random tensor generation using torch.manual_seed",
    "PyTorch Docs: Reproducibility and torch.manual_seed"
)

add_q(
    "PTCA-F-025", A1, "Medium", False,
    "What happens when you try to create a tensor from a jagged (non-rectangular) nested Python list such as `[[1, 2, 3], [4, 5]]`?",
    "import torch\nt = torch.tensor([[1, 2, 3], [4, 5]])",
    {
        "A": "PyTorch pads the shorter row with `0` to create a `(2, 3)` tensor.",
        "B": "PyTorch creates a 1D tensor of Python `list` objects with `dtype=object`.",
        "C": "PyTorch raises a `ValueError: expected sequence of length 3 at dim 1 (got 2)` because standard dense tensors require uniform rectangular dimensions.",
        "D": "PyTorch truncates the longer row to create a `(2, 2)` tensor."
    },
    ["C"],
    "Standard PyTorch strided tensors require uniform sizes along every dimension. Passing a ragged/jagged sequence to `torch.tensor()` raises a `ValueError`.",
    {
        "A": "Incorrect. `torch.tensor()` never implicitly pads ragged sequences (use `torch.nn.utils.rnn.pad_sequence` on a list of 1D tensors for padding).",
        "B": "Incorrect. Unlike NumPy, PyTorch does not support `dtype=object` tensors.",
        "C": "Correct. `torch.tensor()` raises a `ValueError` when nested lists have inconsistent lengths.",
        "D": "Incorrect. `torch.tensor()` never silently truncates input data."
    },
    "Recognize rectangular shape constraints in torch.tensor()",
    "PyTorch Docs: torch.tensor"
)

add_q(
    "PTCA-F-026", A1, "Hard", False,
    "A user already has a tensor `x = torch.tensor([1.0, 2.0], requires_grad=True)`. In downstream code, they write `y = torch.tensor(x)`. What warning does PyTorch emit and what is the recommended idiom to create an independent copy detached from the computation graph?",
    "import torch\nx = torch.tensor([1.0, 2.0], requires_grad=True)\ny = torch.tensor(x)",
    {
        "A": "It emits a `UserWarning` about constructing a tensor from a tensor, and recommends `x.clone().detach()` (or `x.detach().clone()`).",
        "B": "It emits a `DeprecationWarning` and recommends `torch.from_numpy(x)`.",
        "C": "It raises a fatal `RuntimeError` because `torch.tensor()` cannot accept a `Tensor` argument.",
        "D": "It emits no warning and preserves `y.grad_fn` connected to `x`."
    },
    ["A"],
    "Passing an existing `Tensor` to `torch.tensor(x)` triggers `UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor)`.",
    {
        "A": "Correct. PyTorch warns against `torch.tensor(x)` on an existing tensor and recommends `x.clone().detach()` to explicitly copy and detach.",
        "B": "Incorrect. `torch.from_numpy(x)` would fail with a `TypeError` because `x` is a `Tensor`, not a `numpy.ndarray`.",
        "C": "Incorrect. It succeeds and copies the data (with `requires_grad=False`), but emits a `UserWarning`.",
        "D": "Incorrect. `torch.tensor(x)` does not preserve autograd history (`y.requires_grad` is `False` and `y.grad_fn` is `None`), and it emits a `UserWarning`."
    },
    "Follow best practices when copy-constructing from an existing PyTorch tensor",
    "PyTorch Docs: torch.tensor"
)

add_q(
    "PTCA-F-027", A1, "Medium", False,
    "In PyTorch, what is the relationship between the class `torch.Tensor` and `torch.FloatTensor` when creating tensors with default settings?",
    "import torch\nx = torch.zeros(3, 4)\nprint(type(x), isinstance(x, torch.FloatTensor))",
    {
        "A": "`torch.Tensor` is an alias for `torch.DoubleTensor` (64-bit float) by default.",
        "B": "`torch.Tensor` is the main tensor class and is an alias for the default tensor type (`torch.FloatTensor`, 32-bit floating point); `isinstance(x, torch.FloatTensor)` evaluates to `True` for a CPU `float32` tensor.",
        "C": "`torch.FloatTensor` is deprecated and `isinstance(x, torch.FloatTensor)` returns `False`.",
        "D": "`torch.Tensor` creates `int64` tensors by default, so `isinstance(x, torch.FloatTensor)` is `False`."
    },
    ["B"],
    "As taught in Module 2 (`1_tensor_basic.ipynb`), the type of a default tensor returned by factory methods like `torch.zeros(3, 4)` is `torch.Tensor`, which is an alias for `torch.FloatTensor` (populated with 32-bit floating-point numbers by default).",
    {
        "A": "Incorrect. By default, PyTorch uses 32-bit floating-point (`torch.float32` / `torch.FloatTensor`), unlike NumPy which defaults to `float64`.",
        "B": "Correct. By default, `torch.Tensor` corresponds to `torch.FloatTensor` (`torch.float32`), and `isinstance(x, torch.FloatTensor)` is `True`.",
        "C": "Incorrect. `isinstance(x, torch.FloatTensor)` returns `True` for any CPU `float32` tensor.",
        "D": "Incorrect. Factory methods like `torch.zeros`, `torch.ones`, `torch.rand`, and `torch.empty` default to `torch.float32`."
    },
    "Identify default tensor class and 32-bit floating-point convention in PyTorch",
    "modules/module_2_tensors/1_tensor_basic.ipynb"
)

add_q(
    "PTCA-F-028", A1, "Medium", True,
    "Which TWO of the following statements accurately describe how `torch.Tensor.numpy()` interacts with a CPU tensor?",
    "import torch\nt = torch.tensor([1.0, 2.0, 3.0])\narr = t.numpy()",
    {
        "A": "`arr` and `t` share the same underlying memory storage, so modifying `arr[0] = 99.0` also modifies `t[0]`.",
        "B": "`t.numpy()` always allocates a deep copy of the tensor data so that `t` cannot be mutated from NumPy.",
        "C": "If `t.requires_grad` is `True`, calling `t.numpy()` directly raises a `RuntimeError` requiring you to call `t.detach().numpy()` first.",
        "D": "If `t` resides on a CUDA GPU (`device='cuda:0'`), `t.numpy()` automatically copies `t` to CPU and returns the NumPy array."
    },
    ["A", "C"],
    "`t.numpy()` returns a NumPy `ndarray` sharing the same underlying memory buffer on CPU (zero copy). However, if `t.requires_grad` is `True`, PyTorch prevents silent side-effects on tracked tensors by raising `RuntimeError: Can't call numpy() on Tensor that requires grad. Use tensor.detach().numpy() instead.` Also, `t.numpy()` on a CUDA tensor raises an error until `.cpu()` is called.",
    {
        "A": "Correct. On CPU, `.numpy()` returns a zero-copy view sharing storage with the tensor.",
        "B": "Incorrect. `.numpy()` shares storage rather than copying (unless you explicitly call `.numpy().copy()` or `t.clone().numpy()`).",
        "C": "Correct. Tensors that require gradients must be detached via `t.detach().numpy()` before converting to NumPy.",
        "D": "Incorrect. Calling `.numpy()` on a GPU tensor raises `TypeError: can't convert cuda:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.`"
    },
    "Convert PyTorch tensors to NumPy arrays while handling memory sharing and autograd constraints",
    "PyTorch Docs: torch.Tensor.numpy"
)

print(f"Loaded {len(questions)} A1 questions.")

A2 = "A2: Tensor Attributes & Dtypes"

add_q(
    "PTCA-F-029", A2, "Easy", False,
    "What is the difference in usage between `x.shape` and `x.size()` on a PyTorch tensor `x = torch.randn(4, 16, 32)`?",
    "import torch\nx = torch.randn(4, 16, 32)\nprint(x.shape == x.size(), x.size(1), x.size(-1))",
    {
        "A": "`x.shape` is a property returning a `torch.Size` tuple, whereas `x.size()` is a method that returns the same `torch.Size` when called with no arguments or returns a specific dimension's `int` length when passed a `dim` argument (e.g., `x.size(1)`).",
        "B": "`x.shape` returns the tuple of dimensions `(4, 16, 32)`, whereas `x.size()` returns the total number of elements (`2048`) like NumPy's `.size`.",
        "C": "`x.shape` is a method (`x.shape()`), whereas `x.size` is a read-only property.",
        "D": "`x.shape` only works on CPU tensors, whereas `x.size()` works on both CPU and CUDA tensors."
    },
    ["A"],
    "In PyTorch, `x.shape` is an attribute/property (alias for `x.size()`) that returns a `torch.Size` object (a subclass of `tuple`). `x.size()` is a method that can also take an integer dimension index `x.size(dim)` to directly return the size along that axis (`16` for `dim=1`, `32` for `dim=-1`). Note that unlike NumPy where `arr.size` is total element count, in PyTorch total element count is `x.numel()`.",
    {
        "A": "Correct. `x.shape` is an attribute and `x.size(dim=None)` is a method supporting optional dimension indexing.",
        "B": "Incorrect. That is a classic NumPy-to-PyTorch trap: in PyTorch, `x.size()` returns the shape (`torch.Size`), while `x.numel()` returns total element count (`2048`).",
        "C": "Incorrect. `x.shape` is an attribute (not callable), and `x.size()` is a method.",
        "D": "Incorrect. Both `x.shape` and `x.size()` work identically across all devices."
    },
    "Compare .shape attribute and .size() method on PyTorch tensors",
    "modules/module_2_tensors/1_tensor_basic.ipynb"
)

add_q(
    "PTCA-F-030", A2, "Easy", False,
    "What is printed by the following code inspecting tensor rank (`ndim` / `dim()`) and total elements (`numel()`)?",
    "import torch\n\nx = torch.zeros(2, 1, 4, 3)\nprint(x.ndim, x.dim(), x.numel())",
    {
        "A": "4 4 24",
        "B": "3 3 24",
        "C": "4 24 24",
        "D": "24 4 4"
    },
    ["A"],
    "`x.ndim` (attribute) and `x.dim()` (method) both return the number of dimensions (rank) of the tensor, which is `4` (including the singleton dimension of size 1). `x.numel()` returns the product of all dimension sizes: $2 \\times 1 \\times 4 \\times 3 = 24$.",
    {
        "A": "Correct. Both `x.ndim` and `x.dim()` return `4`, and `x.numel()` returns $2 \\times 1 \\times 4 \\times 3 = 24$.",
        "B": "Incorrect. Singleton dimensions of size `1` still count toward tensor rank (`ndim == 4`).",
        "C": "Incorrect. `x.dim()` returns the number of dimensions (`4`), not the number of elements (`24`).",
        "D": "Incorrect. `x.ndim` is `4` and `x.numel()` is `24`."
    },
    "Use .ndim, .dim(), and .numel() to query tensor rank and element count",
    "modules/module_2_tensors/1_tensor_basic.ipynb"
)

add_q(
    "PTCA-F-031", A2, "Medium", False,
    "What happens when you calculate `x.numel()` on a tensor that has a zero-sized dimension, such as `x = torch.empty(4, 0, 8)`?",
    "import torch\nx = torch.empty(4, 0, 8)\nprint(x.ndim, x.numel(), x.element_size(), x.nbytes)",
    {
        "A": "3 0 4 0",
        "B": "2 32 4 128",
        "C": "0 0 0 0",
        "D": "It raises a `RuntimeError` because dimensions of size `0` are not permitted in `torch.empty`."
    },
    ["A"],
    "A tensor with shape `(4, 0, 8)` is a valid 3-dimensional (`ndim=3`) empty tensor. Its total element count is the product of its dimensions ($4 \\times 0 \\times 8 = 0$). Each `float32` element has `element_size() == 4` bytes, and total storage bytes `nbytes == numel() * element_size() == 0`.",
    {
        "A": "Correct. `ndim` is `3`, `numel()` is `0`, `element_size()` for default `float32` is `4`, and `nbytes` is `0 * 4 = 0`.",
        "B": "Incorrect. A zero in any dimension makes the total product of elements `0`, not `32`.",
        "C": "Incorrect. Even when `numel()` is `0`, the tensor still has 3 dimensions (`ndim=3`) and a `float32` dtype (`element_size()=4`).",
        "D": "Incorrect. PyTorch supports 0-sized dimensions (e.g., in `modules/module_2_tensors/4_tensor_broadcasting.ipynb`, `torch.empty((0,))`)."
    },
    "Analyze rank, element count, and byte size for tensors with zero-length dimensions",
    "modules/module_2_tensors/4_tensor_broadcasting.ipynb"
)

add_q(
    "PTCA-F-032", A2, "Medium", False,
    "A tensor `t` is created with `t = torch.zeros(10, 20, dtype=torch.float64)`. What are the values of `t.element_size()` and `t.nbytes`?",
    "import torch\nt = torch.zeros(10, 20, dtype=torch.float64)\nprint(t.element_size(), t.nbytes)",
    {
        "A": "8 1600",
        "B": "4 800",
        "C": "64 12800",
        "D": "8 200"
    },
    ["A"],
    "`torch.float64` (`torch.double`) uses 64 bits = `8` bytes per element (`t.element_size() == 8`). With $10 \\times 20 = 200$ elements, `t.nbytes` (which equals `t.numel() * t.element_size()`) is $200 \\times 8 = 1600$ bytes.",
    {
        "A": "Correct. Each `float64` element occupies 8 bytes, and $200 \\times 8 = 1600$ total bytes.",
        "B": "Incorrect. `4` bytes and `800` total bytes correspond to `torch.float32`, not `torch.float64`.",
        "C": "Incorrect. `element_size()` returns size in bytes (`8`), not bits (`64`).",
        "D": "Incorrect. `200` is `t.numel()`, whereas `t.nbytes` multiplies element count by byte size (`1600`)."
    },
    "Calculate memory footprint using .element_size() and .nbytes",
    "PyTorch Docs: torch.Tensor.element_size and torch.Tensor.nbytes"
)

add_q(
    "PTCA-F-033", A2, "Easy", False,
    "Which option correctly pairs the standard floating-point and complex `torch.dtype` objects with their official shorthand aliases in PyTorch?",
    "",
    {
        "A": "`torch.float16` == `torch.half`, `torch.float32` == `torch.float`, `torch.float64` == `torch.double`, `torch.complex64` == `torch.cfloat`, `torch.complex128` == `torch.cdouble`",
        "B": "`torch.float16` == `torch.short`, `torch.float32` == `torch.single`, `torch.float64` == `torch.long`, `torch.complex64` == `torch.chalf`",
        "C": "`torch.bfloat16` == `torch.half`, `torch.float32` == `torch.double`, `torch.float64` == `torch.quad`",
        "D": "`torch.float16` == `torch.bfloat16`, `torch.complex64` == `torch.cdouble`, `torch.complex128` == `torch.cfloat`"
    },
    ["A"],
    "As documented in Module 2 (`2_tensor_attributes.ipynb`), PyTorch defines aliases: `torch.half` (`torch.float16`), `torch.float` (`torch.float32`), `torch.double` (`torch.float64`), `torch.cfloat` (`torch.complex64`), and `torch.cdouble` (`torch.complex128`).",
    {
        "A": "Correct. Every floating-point and complex alias matches its exact bit-width counterpart.",
        "B": "Incorrect. `torch.short` (`int16`) and `torch.long` (`int64`) are signed integer types, and `torch.single` does not exist.",
        "C": "Incorrect. `torch.half` is `torch.float16` (IEEE 754 half precision), NOT `torch.bfloat16`.",
        "D": "Incorrect. `float16` and `bfloat16` are distinct 16-bit formats, and `complex64` (two 32-bit floats) is `cfloat`, while `complex128` (two 64-bit floats) is `cdouble`."
    },
    "Map floating-point and complex dtypes to their canonical PyTorch aliases",
    "modules/module_2_tensors/2_tensor_attributes.ipynb"
)

add_q(
    "PTCA-F-034", A2, "Easy", False,
    "Which option correctly pairs all integer and boolean `torch.dtype` types with their bit-widths and aliases?",
    "",
    {
        "A": "`torch.uint8` (8-bit unsigned), `torch.int8` (8-bit signed), `torch.int16`/`torch.short` (16-bit signed), `torch.int32`/`torch.int` (32-bit signed), `torch.int64`/`torch.long` (64-bit signed), `torch.bool` (boolean)",
        "B": "`torch.uint8` (8-bit signed), `torch.int16`/`torch.half` (16-bit signed), `torch.int32`/`torch.long` (32-bit signed), `torch.int64`/`torch.double` (64-bit signed)",
        "C": "`torch.int` is an alias for `torch.int64` on 64-bit operating systems, and `torch.short` is `torch.int8`.",
        "D": "`torch.long` is 128-bit integer and `torch.int` is 64-bit integer."
    },
    ["A"],
    "In PyTorch (`2_tensor_attributes.ipynb`), the integer and boolean dtypes are: `torch.uint8` (8-bit unsigned), `torch.int8` (8-bit signed), `torch.int16` or `torch.short` (16-bit signed), `torch.int32` or `torch.int` (32-bit signed), `torch.int64` or `torch.long` (64-bit signed), and `torch.bool`.",
    {
        "A": "Correct. Matches all integer and boolean dtypes and aliases (`short`, `int`, `long`) in PyTorch.",
        "B": "Incorrect. `torch.half` (`float16`) and `torch.double` (`float64`) are floating-point types, and `torch.long` is 64-bit (`int64`), not 32-bit.",
        "C": "Incorrect. In PyTorch, `torch.int` is always `torch.int32` (32-bit) and `torch.long` is always `torch.int64` (64-bit) regardless of OS.",
        "D": "Incorrect. `torch.long` is 64-bit (`int64`) and `torch.int` is 32-bit (`int32`)."
    },
    "Identify integer and boolean dtypes and their aliases (short, int, long)",
    "modules/module_2_tensors/2_tensor_attributes.ipynb"
)

add_q(
    "PTCA-F-035", A2, "Medium", False,
    "What is the output of the following code comparing `torch.float16` (`half`) and `torch.bfloat16` on a large scalar value `1e7`?",
    "import torch\n\na = torch.tensor(1e7, dtype=torch.float32)\nb = torch.tensor(1e7, dtype=torch.float16)\nc = torch.tensor(1e7, dtype=torch.bfloat16)\nprint(torch.isinf(a).item(), torch.isinf(b).item(), torch.isinf(c).item())",
    {
        "A": "False True False",
        "B": "False True True",
        "C": "False False False",
        "D": "False False True"
    },
    ["A"],
    "IEEE 754 `float16` uses 5 exponent bits and 10 mantissa bits, giving a maximum finite representable value of `65504.0`; therefore `1e7` overflows to `inf` (`torch.isinf(b)` is `True`), as demonstrated in Module 2 (`2_tensor_attributes.ipynb`). `bfloat16` uses 8 exponent bits (the exact same exponent bit-width as `float32`) and 7 mantissa bits, so it maintains the same dynamic range as `float32` (`~3.4e38`) and represents `1e7` without overflowing (`False`).",
    {
        "A": "Correct. `float16` overflows to `inf` on `1e7` (`True`), whereas both `float32` and `bfloat16` have 8 exponent bits and represent `1e7` as a finite number (`False`).",
        "B": "Incorrect. `bfloat16` has the same dynamic range as `float32` and does not overflow at `1e7`.",
        "C": "Incorrect. `float16` overflows to `inf` for any value above `65504`.",
        "D": "Incorrect. `float16` has narrower dynamic range than `bfloat16`, not wider."
    },
    "Contrast dynamic range and overflow behavior of float16 versus bfloat16 and float32",
    "modules/module_2_tensors/2_tensor_attributes.ipynb"
)

add_q(
    "PTCA-F-036", A2, "Medium", False,
    "While `torch.bfloat16` preserves the dynamic range of `torch.float32`, what is the trade-off compared to `torch.float16` for numbers within the normal range (e.g., `1.0 + 1e-3`)?",
    "import torch\n\nf16 = torch.tensor(1.001, dtype=torch.float16)\nbf16 = torch.tensor(1.001, dtype=torch.bfloat16)\nprint(round(f16.item(), 4), round(bf16.item(), 4))",
    {
        "A": "1.001 1.0",
        "B": "1.0 1.001",
        "C": "1.001 1.001",
        "D": "1.0 1.0"
    },
    ["A"],
    "Both `float16` and `bfloat16` use 16 bits total (1 sign bit + 15 bits). `float16` allocates 10 bits to the fraction/mantissa (machine epsilon $\\approx 9.77 \\times 10^{-4}$), so `1.001` is distinct from `1.0`. `bfloat16` allocates 8 bits to the exponent and only 7 bits to the mantissa (machine epsilon $2^{-7} = 0.0078125$), so `1.001` rounds to `1.0`.",
    {
        "A": "Correct. `float16` has 10 mantissa bits and preserves `1.001`, whereas `bfloat16` has only 7 mantissa bits and rounds `1.001` to `1.0`.",
        "B": "Incorrect. `bfloat16` trades mantissa precision (7 bits vs 10 bits) in exchange for a wider exponent range (8 bits vs 5 bits).",
        "C": "Incorrect. `bfloat16`'s minimum step above `1.0` is $2^{-7} \\approx 0.0078$, so `1.001` cannot be distinguished from `1.0`.",
        "D": "Incorrect. `float16`'s step above `1.0` is $2^{-10} \\approx 0.000977$, so it accurately represents `1.001`."
    },
    "Understand mantissa precision versus exponent range trade-offs in 16-bit floating-point formats",
    "modules/module_2_tensors/2_tensor_attributes.ipynb"
)

add_q(
    "PTCA-F-037", A2, "Medium", False,
    "What are the element byte sizes (`element_size()`) of `torch.complex64` (`torch.cfloat`) and `torch.complex128` (`torch.cdouble`), and what is the dtype of `z.real` when `z` has dtype `torch.complex64`?",
    "import torch\nz64 = torch.tensor([1.0 + 2.0j], dtype=torch.complex64)\nz128 = torch.tensor([1.0 + 2.0j], dtype=torch.complex128)\nprint(z64.element_size(), z128.element_size(), z64.real.dtype)",
    {
        "A": "8 16 torch.float32",
        "B": "4 8 torch.float32",
        "C": "8 16 torch.float64",
        "D": "64 128 torch.complex32"
    },
    ["A"],
    "`torch.complex64` is a 64-bit complex number (8 bytes total) composed of two 32-bit `torch.float32` components (`real` and `imag`). `torch.complex128` is a 128-bit complex number (16 bytes total) composed of two 64-bit `torch.float64` components.",
    {
        "A": "Correct. `complex64` is 8 bytes (two `float32`s, so `z64.real.dtype` is `torch.float32`) and `complex128` is 16 bytes (two `float64`s).",
        "B": "Incorrect. `64` and `128` in `complex64`/`complex128` refer to total bits across both real and imaginary parts (8 bytes and 16 bytes).",
        "C": "Incorrect. The real and imaginary components of a `complex64` tensor each take 32 bits (`torch.float32`), not `torch.float64`.",
        "D": "Incorrect. `element_size()` returns bytes (`8` and `16`), not bits (`64` and `128`)."
    },
    "Inspect complex tensor storage sizes and component dtypes",
    "modules/module_2_tensors/2_tensor_attributes.ipynb"
)

add_q(
    "PTCA-F-038", A2, "Easy", False,
    "What is printed by the following calls to `torch.is_floating_point()` and `torch.is_complex()`?",
    "import torch\n\nt_bf16 = torch.ones(2, dtype=torch.bfloat16)\nt_int = torch.ones(2, dtype=torch.int64)\nt_comp = torch.ones(2, dtype=torch.cfloat)\n\nprint(torch.is_floating_point(t_bf16), torch.is_floating_point(t_comp), torch.is_complex(t_comp), torch.is_floating_point(t_int))",
    {
        "A": "True False True False",
        "B": "True True True False",
        "C": "False False True False",
        "D": "True False False True"
    },
    ["A"],
    "`torch.is_floating_point(tensor)` returns `True` if the tensor's dtype is one of the real floating-point types (`float64`, `float32`, `float16`, `bfloat16`), and `False` for complex types (`cfloat`/`cdouble`) and integer/boolean types. `torch.is_complex(tensor)` returns `True` for complex dtypes (`complex64`, `complex128`, `complex32`).",
    {
        "A": "Correct. `bfloat16` is floating point (`True`), `cfloat` is complex (`is_floating_point=False`, `is_complex=True`), and `int64` is integer (`False`).",
        "B": "Incorrect. `torch.is_floating_point()` returns `False` for complex tensors; complex types are checked via `torch.is_complex()`.",
        "C": "Incorrect. `torch.bfloat16` is a floating-point dtype, so `torch.is_floating_point(t_bf16)` is `True`.",
        "D": "Incorrect. `t_comp` is complex (`True`) and `t_int` is not floating-point (`False`)."
    },
    "Check tensor dtype families with torch.is_floating_point and torch.is_complex",
    "modules/module_2_tensors/2_tensor_attributes.ipynb"
)

add_q(
    "PTCA-F-039", A2, "Medium", False,
    "How does `torch.is_nonzero(x)` behave when called on different tensors?",
    "import torch\n\na = torch.tensor(0.0)\nb = torch.tensor([5])\nc = torch.tensor([1, 2])",
    {
        "A": "`torch.is_nonzero(a)` returns `False`, `torch.is_nonzero(b)` returns `True`, and `torch.is_nonzero(c)` raises a `RuntimeError` because `is_nonzero` only accepts single-element tensors (`numel() == 1`).",
        "B": "`torch.is_nonzero(c)` returns a boolean tensor `tensor([True, True])`.",
        "C": "`torch.is_nonzero(b)` raises a `RuntimeError` because `b` is 1D rather than 0D.",
        "D": "`torch.is_nonzero` returns the indices of non-zero elements, identical to `torch.nonzero`."
    },
    ["A"],
    "`torch.is_nonzero(input)` returns a Python `bool` (`True` or `False`) indicating whether a single-element tensor (`input.numel() == 1`) is not equal to zero after casting to a scalar. If `input.numel() != 1` (like `c` with 2 elements), it raises `RuntimeError: Boolean value of Tensor with more than one value is ambiguous`.",
    {
        "A": "Correct. `torch.is_nonzero` returns a Python `bool` for any single-element tensor (`a` -> `False`, `b` -> `True`) and raises a `RuntimeError` for multi-element tensors (`c`).",
        "B": "Incorrect. `torch.is_nonzero` returns a single Python `bool`, not an element-wise boolean mask (use `c != 0` for element-wise comparison).",
        "C": "Incorrect. `b` has `numel() == 1`, which is allowed by `torch.is_nonzero`.",
        "D": "Incorrect. `torch.nonzero(x)` returns the indices of non-zero elements, whereas `torch.is_nonzero(x)` tests truthiness of a single-element tensor."
    },
    "Understand single-element semantics of torch.is_nonzero",
    "PyTorch Docs: torch.is_nonzero"
)

add_q(
    "PTCA-F-040", A2, "Medium", False,
    "According to PyTorch's type promotion hierarchy (`bool < int < float < complex`), what are the output dtypes of the three expressions below?",
    "import torch\n\nb = torch.tensor([True, False], dtype=torch.bool)\ni = torch.tensor([1, 2], dtype=torch.int32)\nf = torch.tensor([1.0, 2.0], dtype=torch.float16)\nc = torch.tensor([1.0 + 0j, 2.0 + 0j], dtype=torch.complex64)\n\nprint((b + i).dtype, (i + f).dtype, (f + c).dtype)",
    {
        "A": "torch.int32 torch.float16 torch.complex64",
        "B": "torch.bool torch.float32 torch.complex128",
        "C": "torch.int64 torch.int32 torch.float16",
        "D": "torch.int32 torch.float32 torch.complex64"
    },
    ["A"],
    "When combining tensors across category families (`bool < int < float < complex`), the lower category promotes to the higher category's dtype: `bool + int32 -> int32`, `int32 + float16 -> float16` (in PyTorch, integer tensors promote to the floating-point tensor's existing dtype rather than widening `float16` to `float32`), and `float16 + complex64 -> complex64`.",
    {
        "A": "Correct. `bool + int32` gives `torch.int32`, `int32 + float16` gives `torch.float16`, and `float16 + complex64` gives `torch.complex64`.",
        "B": "Incorrect. `bool` promotes to `int32`, and in PyTorch `int32 + float16` stays `float16`.",
        "C": "Incorrect. `int + float` promotes to float (`float16`), and `float + complex` promotes to complex (`complex64`).",
        "D": "Incorrect. PyTorch's `promote_types(torch.int32, torch.float16)` evaluates to `torch.float16`, not `torch.float32`."
    },
    "Predict result dtypes under PyTorch's cross-category type promotion rules",
    "PyTorch Docs: Tensor Attributes - Type Promotion Documentation (torch.promote_types)"
)

add_q(
    "PTCA-F-041", A2, "Hard", False,
    "What does `torch.promote_types(torch.float16, torch.bfloat16)` return when a `float16` tensor and a `bfloat16` tensor are added together?",
    "import torch\n\na = torch.ones(2, dtype=torch.float16)\nb = torch.ones(2, dtype=torch.bfloat16)\nc = a + b\nprint(c.dtype)",
    {
        "A": "torch.float32",
        "B": "torch.bfloat16",
        "C": "torch.float16",
        "D": "It raises a `RuntimeError` because `float16` and `bfloat16` cannot be promoted."
    },
    ["A"],
    "Neither `float16` (10 mantissa bits, 5 exponent bits) nor `bfloat16` (7 mantissa bits, 8 exponent bits) is a subset of the other. To preserve both the dynamic range of `bfloat16` and the mantissa precision of `float16`, PyTorch promotes `float16 + bfloat16` to `torch.float32`.",
    {
        "A": "Correct. Promoting `float16` and `bfloat16` yields `torch.float32`.",
        "B": "Incorrect. Converting to `bfloat16` would lose 3 bits of mantissa precision from `float16`.",
        "C": "Incorrect. Converting to `float16` would lose 3 bits of exponent dynamic range from `bfloat16`.",
        "D": "Incorrect. PyTorch automatically promotes mixed `float16` and `bfloat16` operands to `torch.float32`."
    },
    "Understand type promotion between float16 and bfloat16",
    "PyTorch Docs: torch.promote_types"
)

add_q(
    "PTCA-F-042", A2, "Medium", False,
    "What is the output of dividing two integer tensors using true division `/` versus floor division `//` in PyTorch?",
    "import torch\n\nx = torch.tensor([7, -7], dtype=torch.int64)\ny = torch.tensor([2, 2], dtype=torch.int64)\n\ntrue_div = x / y\nfloor_div = x // y\nprint(true_div.dtype, true_div.tolist(), floor_div.dtype, floor_div.tolist())",
    {
        "A": "torch.float32 [3.5, -3.5] torch.int64 [3, -4]",
        "B": "torch.int64 [3, -3] torch.int64 [3, -4]",
        "C": "torch.float64 [3.5, -3.5] torch.int64 [3, -3]",
        "D": "torch.float32 [3.5, -3.5] torch.float32 [3.0, -4.0]"
    },
    ["A"],
    "In modern PyTorch, true division `/` on integer tensors always promotes to the default floating-point type (`torch.float32`), yielding `[3.5, -3.5]`. Floor division `//` preserves the integer dtype (`torch.int64`) and rounds toward $-\infty$ (like Python's `//`), so `-7 // 2` is `-4` (note: `torch.div(x, y, rounding_mode='trunc')` rounds toward zero to `-3`).",
    {
        "A": "Correct. `/` promotes `int64` to `torch.float32` (`[3.5, -3.5]`), while `//` keeps `torch.int64` and floors toward $-\infty$ (`[3, -4]`).",
        "B": "Incorrect. `/` performs true floating-point division in PyTorch, not integer truncation.",
        "C": "Incorrect. `/` promotes integers to `torch.get_default_dtype()` (`torch.float32`), and `-7 // 2` floors to `-4`, not `-3`.",
        "D": "Incorrect. `//` on integer tensors returns an integer tensor (`torch.int64`), not `torch.float32`."
    },
    "Distinguish true division (/) and floor division (//) on integer tensors",
    "PyTorch Docs: torch.div and Tensor arithmetic operators"
)

add_q(
    "PTCA-F-043", A2, "Medium", False,
    "How does casting a floating-point tensor to an integer dtype via `.to(torch.int32)` (or `.int()`) convert fractional values?",
    "import torch\n\nx = torch.tensor([2.9, -2.9, 1.5, -1.5])\ny = x.to(torch.int32)\nprint(y.tolist())",
    {
        "A": "[2, -2, 1, -1]",
        "B": "[3, -3, 2, -2]",
        "C": "[2, -3, 1, -2]",
        "D": "It raises a `RuntimeError` unless `torch.round(x)` is called first."
    },
    ["A"],
    "Casting floating-point tensors to integer dtypes with `.to(torch.int32)` or `.int()` truncates fractional parts toward zero (just like `int(2.9) -> 2` and `int(-2.9) -> -2` in Python/C++), rather than rounding to nearest or flooring toward $-\infty$.",
    {
        "A": "Correct. `.to(torch.int32)` truncates toward zero, turning `2.9 -> 2`, `-2.9 -> -2`, `1.5 -> 1`, and `-1.5 -> -1`.",
        "B": "Incorrect. `.to(int)` does not round to the nearest integer; use `torch.round(x).to(torch.int32)` if rounding is desired.",
        "C": "Incorrect. `[2, -3, 1, -2]` would be floor toward $-\infty$ (`torch.floor(x)`), not truncation toward zero.",
        "D": "Incorrect. `.to(torch.int32)` is a valid cast operation that truncates without raising an error."
    },
    "Understand truncation-toward-zero semantics when casting floats to integers via .to(dtype)",
    "PyTorch Docs: torch.Tensor.to"
)

add_q(
    "PTCA-F-044", A2, "Medium", False,
    "A developer creates a NumPy array of features `X_np = np.random.randn(8, 4)`, converts it via `X = torch.from_numpy(X_np)`, and passes `X` directly into `layer = torch.nn.Linear(4, 2)`. Why does `layer(X)` fail with a `RuntimeError`?",
    "import numpy as np\nimport torch\nimport torch.nn as nn\n\nX_np = np.random.randn(8, 4)\nX = torch.from_numpy(X_np)\nlayer = nn.Linear(4, 2)\nout = layer(X)",
    {
        "A": "`np.random.randn` defaults to 64-bit float (`float64` / `torch.double`), whereas `nn.Linear` parameters default to 32-bit float (`torch.float32`), causing `RuntimeError: mat1 and mat2 must have the same dtype, got Double and Float`.",
        "B": "`torch.from_numpy` creates a read-only tensor that cannot be multiplied by `nn.Linear` weights.",
        "C": "`nn.Linear(4, 2)` expects input shape `(4, 8)` instead of `(8, 4)`.",
        "D": "`torch.from_numpy` places the tensor on CUDA while `nn.Linear` is on CPU."
    },
    ["A"],
    "In NumPy, floating-point arrays default to `np.float64`, which `torch.from_numpy` preserves as `torch.float64` (`Double`). In PyTorch, `nn.Module` layers initialize weights in `torch.get_default_dtype()`, which is `torch.float32` (`Float`). Linear algebra ops like `matmul`/`addmm` inside `nn.Linear` do not auto-promote mismatched `Double` and `Float` tensors, raising a `RuntimeError`. Casting `X = torch.from_numpy(X_np).float()` (or `X_np.astype(np.float32)`) fixes the bug.",
    {
        "A": "Correct. NumPy defaults to `float64` (`Double`) while PyTorch modules default to `float32` (`Float`), causing a dtype mismatch in `nn.Linear`.",
        "B": "Incorrect. `np.random.randn` returns a writable array, and `from_numpy` produces a normal writable tensor.",
        "C": "Incorrect. `nn.Linear(in_features=4, out_features=2)` expects trailing dimension `4`, so `(8, 4)` is the valid shape.",
        "D": "Incorrect. Both `torch.from_numpy` and `nn.Linear` reside on CPU by default."
    },
    "Resolve the classic NumPy float64 to PyTorch nn.Module float32 dtype mismatch",
    "modules/module_2_tensors/1_tensor_basic.ipynb"
)

add_q(
    "PTCA-F-045", A2, "Easy", False,
    "Which functions get and set PyTorch's global default floating-point data type, and what restriction applies to the argument of `torch.set_default_dtype(d)`?",
    "import torch\nprint(torch.get_default_dtype())",
    {
        "A": "`torch.get_default_dtype()` and `torch.set_default_dtype(d)`; `d` must be a floating-point `torch.dtype` (such as `torch.float64`, `torch.float16`, or `torch.bfloat16`), and passing an integer dtype like `torch.int64` raises a `TypeError`.",
        "B": "`torch.get_dtype()` and `torch.set_dtype(d)`; `d` can be any of the 12 PyTorch dtypes including `torch.int64` and `torch.bool`.",
        "C": "`torch.default_dtype` is a read-only constant fixed at `torch.float32` that cannot be changed at runtime.",
        "D": "`torch.set_default_dtype(torch.int32)` changes `torch.zeros(3)` to produce 32-bit integers."
    },
    ["A"],
    "`torch.get_default_dtype()` returns the current default floating-point dtype (`torch.float32` initially). `torch.set_default_dtype(d)` updates the default floating-point dtype used by factory functions and `nn.Module` parameters, and only accepts floating-point dtypes (passing `torch.int64` raises `TypeError: only floating-point types are supported as the default type`).",
    {
        "A": "Correct. `get_default_dtype()` and `set_default_dtype()` manage the default floating-point dtype, and non-floating-point dtypes are rejected.",
        "B": "Incorrect. `torch.get_dtype` does not exist, and integer/boolean dtypes cannot be set as the default dtype.",
        "C": "Incorrect. The default floating-point dtype can be changed dynamically via `torch.set_default_dtype()`.",
        "D": "Incorrect. Passing `torch.int32` to `torch.set_default_dtype` raises a `TypeError`."
    },
    "Inspect and configure global floating-point dtype with get_default_dtype and set_default_dtype",
    "PyTorch Docs: torch.get_default_dtype and torch.set_default_dtype"
)

add_q(
    "PTCA-F-046", A2, "Medium", False,
    "For which tensor data types (`dtype`) does PyTorch allow setting `requires_grad=True`?",
    "import torch\n# Which tensors can track gradients in autograd?",
    {
        "A": "Only floating-point and complex dtypes (e.g., `float32`, `float64`, `float16`, `bfloat16`, `complex64`, `complex128`); attempting `requires_grad=True` on integer or boolean tensors raises a `RuntimeError`.",
        "B": "Only `torch.float32` and `torch.float64`; half-precision (`float16`, `bfloat16`) and complex tensors cannot track gradients.",
        "C": "All numeric dtypes including `torch.int32` and `torch.int64`, excluding only `torch.bool`.",
        "D": "All 12 PyTorch dtypes support `requires_grad=True`."
    },
    ["A"],
    "Continuous differentiation requires continuous values. PyTorch only allows `requires_grad=True` on floating-point and complex tensors. Attempting `torch.tensor([1, 2], dtype=torch.int64, requires_grad=True)` raises `RuntimeError: Only Tensors of floating point and complex dtype can require gradients`.",
    {
        "A": "Correct. Only floating-point and complex tensors can have `requires_grad=True`; integer and boolean tensors raise a `RuntimeError`.",
        "B": "Incorrect. `float16`, `bfloat16`, `complex64`, and `complex128` all support `requires_grad=True`.",
        "C": "Incorrect. Integer dtypes (`int8`, `uint8`, `int16`, `int32`, `int64`) cannot require gradients.",
        "D": "Incorrect. Integer and boolean tensors cannot have `requires_grad=True`."
    },
    "Enforce floating-point/complex dtype requirements for autograd gradient tracking",
    "modules/module_2_tensors/3_tensor_operations.ipynb"
)

add_q(
    "PTCA-F-047", A2, "Medium", False,
    "A contiguous 3D tensor `x` is created with `x = torch.empty(2, 3, 4)`. What does `x.stride()` return, and what do those numbers represent?",
    "import torch\nx = torch.empty(2, 3, 4)\nprint(x.stride())",
    {
        "A": "`(12, 4, 1)`, representing the number of elements (not bytes) to step in 1D storage to advance by 1 index along dimension 0, dimension 1, and dimension 2 respectively.",
        "B": "`(48, 16, 4)`, representing the number of bytes to step in memory along each dimension.",
        "C": "`(1, 3, 6)`, representing column-major (Fortran-order) element strides.",
        "D": "`(2, 3, 4)`, which is an alias for `x.shape`."
    },
    ["A"],
    "In PyTorch, `.stride()` returns a tuple of element steps (not byte steps) required in the flat 1D storage to move by one position along each dimension. For a contiguous row-major (C-order) tensor of shape `(d0, d1, d2) = (2, 3, 4)`, the strides are `(d1 * d2, d2, 1) = (12, 4, 1)`.",
    {
        "A": "Correct. Contiguous row-major strides for `(2, 3, 4)` are `(3*4, 4, 1) = (12, 4, 1)` measured in elements.",
        "B": "Incorrect. Unlike NumPy's `.strides` (which reports bytes), PyTorch's `.stride()` reports element counts.",
        "C": "Incorrect. PyTorch tensors default to row-major (C-contiguous) layout where the last dimension has stride `1`.",
        "D": "Incorrect. `(2, 3, 4)` is `x.size()`, whereas `x.stride()` is `(12, 4, 1)`."
    },
    "Calculate and interpret tensor strides in row-major strided memory layout",
    "PyTorch Docs: torch.Tensor.stride and tensor_attributes.html"
)

add_q(
    "PTCA-F-048", A2, "Easy", False,
    "What is the default `layout` attribute of a standard dense PyTorch tensor (e.g., `x = torch.zeros(3, 3)`), and what alternative layout represents sparse tensors storing indices and values?",
    "import torch\nx = torch.zeros(3, 3)\nprint(x.layout)",
    {
        "A": "`torch.strided` for standard dense tensors, and `torch.sparse_coo` (or CSR/CSC/BSR/BSC variants) for sparse tensors.",
        "B": "`torch.dense` for standard tensors, and `torch.sparse` for sparse tensors.",
        "C": "`torch.contiguous_format` for standard tensors, and `torch.channels_last` for sparse tensors.",
        "D": "`torch.row_major` for standard tensors, and `torch.col_major` for transposed tensors."
    },
    ["A"],
    "Every standard dense PyTorch tensor has `x.layout == torch.strided`. Sparse coordinate tensors use `torch.sparse_coo` (along with compressed sparse layouts like `torch.sparse_csr`). Note that `torch.contiguous_format` and `torch.channels_last` are `torch.memory_format` objects, not `torch.layout` objects.",
    {
        "A": "Correct. Standard dense tensors use `torch.strided` layout, while sparse coordinate tensors use `torch.sparse_coo`.",
        "B": "Incorrect. Neither `torch.dense` nor `torch.sparse` is a `torch.layout` object.",
        "C": "Incorrect. `torch.contiguous_format` and `torch.channels_last` are `torch.memory_format` values, not `torch.layout` values.",
        "D": "Incorrect. Both row-major and transposed views are represented via strides within `torch.strided` layout."
    },
    "Identify torch.layout values (torch.strided vs torch.sparse_coo)",
    "modules/module_2_tensors/2_tensor_attributes.ipynb"
)

add_q(
    "PTCA-F-049", A2, "Easy", True,
    "Which TWO of the following are valid ways to construct a `torch.device` object pointing to the second CUDA GPU (index `1`)?",
    "import torch\n# Construct a torch.device for GPU index 1",
    {
        "A": "torch.device('cuda:1')",
        "B": "torch.device('cuda', 1)",
        "C": "torch.device(1, 'cuda')",
        "D": "torch.cuda.device_object(1)"
    },
    ["A", "B"],
    "As explained in Module 2 (`2_tensor_attributes.ipynb`), a `torch.device` can be constructed either via a single device string including ordinal (`torch.device('cuda:1')`) or via a device type string and integer device ordinal (`torch.device('cuda', 1)`).",
    {
        "A": "Correct. `torch.device('cuda:1')` parses the device type `'cuda'` and index `1`.",
        "B": "Correct. `torch.device('cuda', 1)` specifies type `'cuda'` and ordinal `1` as separate arguments.",
        "C": "Incorrect. The device type string must be the first argument (`type, index`), not `(index, type)`.",
        "D": "Incorrect. `torch.cuda.device_object` is not a valid PyTorch API."
    },
    "Construct torch.device objects using string or (type, ordinal) signatures",
    "modules/module_2_tensors/2_tensor_attributes.ipynb"
)

add_q(
    "PTCA-F-050", A2, "Medium", False,
    "What is the output of the following code inspecting the `type` and `index` attributes of `torch.device` objects?",
    "import torch\n\nd1 = torch.device('cpu')\nd2 = torch.device('cuda')\nd3 = torch.device('cuda:0')\nprint(d1.type, d2.index, d3.index, d2 == d3)",
    {
        "A": "cpu None 0 False",
        "B": "cpu 0 0 True",
        "C": "cpu -1 0 False",
        "D": "CPU None 0 True"
    },
    ["A"],
    "When a `torch.device` is constructed without an explicit ordinal (e.g., `torch.device('cuda')`), its `.index` attribute is `None`, whereas `torch.device('cuda:0').index` is `0`. Consequently, `torch.device('cuda') == torch.device('cuda:0')` evaluates to `False` because one has `index=None` and the other has `index=0`!",
    {
        "A": "Correct. `d1.type` is `'cpu'`, `d2.index` is `None`, `d3.index` is `0`, and `d2 == d3` is `False`.",
        "B": "Incorrect. `torch.device('cuda')` does not resolve `.index` to `0` until allocated on a tensor; as a `device` object, `d2.index` is `None` and `d2 != d3`.",
        "C": "Incorrect. Unspecified device index is `None`, not `-1`.",
        "D": "Incorrect. `.type` is lowercase `'cpu'`, and `d2 == d3` is `False`."
    },
    "Understand torch.device .type, .index, and equality comparison pitfalls",
    "modules/module_2_tensors/2_tensor_attributes.ipynb"
)

add_q(
    "PTCA-F-051", A2, "Medium", False,
    "Under what condition does `y = x.to(dtype=torch.float32)` return the exact same tensor object (`y is x`) without allocating new memory?",
    "import torch\n\nx = torch.ones(4, dtype=torch.float32)\ny = x.to(dtype=torch.float32)\nz = x.to(dtype=torch.float32, copy=True)\nprint(y is x, z is x)",
    {
        "A": "True False",
        "B": "False False",
        "C": "True True",
        "D": "False True"
    },
    ["A"],
    "When `.to()` is called and the tensor already has the requested `dtype` and `device` (and `copy=False`, which is the default), `.to()` is a no-op and returns `self` (`y is x` is `True`). Passing `copy=True` forces a new tensor allocation (`z is x` is `False`).",
    {
        "A": "Correct. By default (`copy=False`), `.to()` returns `x` itself when `dtype` and `device` already match, whereas `copy=True` forces a copy.",
        "B": "Incorrect. `.to()` avoids unnecessary copies when the target `dtype` and `device` match the source tensor.",
        "C": "Incorrect. `copy=True` guarantees a newly allocated tensor (`z is x` is `False`).",
        "D": "Incorrect. `y is x` is `True` and `z is x` is `False`."
    },
    "Optimize memory usage by understanding no-op vs copy behavior of Tensor.to()",
    "PyTorch Docs: torch.Tensor.to"
)

add_q(
    "PTCA-F-052", A2, "Medium", False,
    "What happens when `-1` is stored into an unsigned 8-bit integer tensor (`torch.uint8`) via `.to(torch.uint8)`?",
    "import torch\nx = torch.tensor([-1, 0, 255, 256], dtype=torch.int32)\ny = x.to(torch.uint8)\nprint(y.tolist())",
    {
        "A": "[255, 0, 255, 0]",
        "B": "[0, 0, 255, 255]",
        "C": "[-1, 0, 255, 256]",
        "D": "It raises an `OverflowError` during `.to(torch.uint8)`."
    },
    ["A"],
    "`torch.uint8` represents values in `[0, 255]` using 8-bit modular (two's complement) wraparound when cast from wider integer types via `.to(torch.uint8)`: `-1 mod 256 == 255`, and `256 mod 256 == 0` (to clamp instead of wrapping, use `x.clamp(0, 255).to(torch.uint8)`).",
    {
        "A": "Correct. Casting `int32` to `uint8` wraps modulo 256: `-1` becomes `255` and `256` becomes `0`.",
        "B": "Incorrect. `.to(torch.uint8)` does not saturate/clamp to `[0, 255]`; you must explicitly call `.clamp(0, 255)` before `.to(torch.uint8)` for saturation.",
        "C": "Incorrect. An 8-bit unsigned integer cannot hold `-1` or `256`.",
        "D": "Incorrect. `.to(torch.uint8)` performs C-style modular truncation of the lower 8 bits without raising `OverflowError`."
    },
    "Recognize modular wraparound when casting signed/wider integers to torch.uint8",
    "PyTorch Docs: torch.uint8 and Tensor.to"
)

add_q(
    "PTCA-F-053", A2, "Easy", False,
    "How can you programmatically query the minimum/maximum finite representable values and machine epsilon of a floating-point dtype like `torch.float16`, or the bounds of an integer dtype like `torch.int16`?",
    "import torch\n# Query numerical limits of float16 and int16",
    {
        "A": "`torch.finfo(torch.float16)` (with `.min`, `.max`, `.eps`) and `torch.iinfo(torch.int16)` (with `.min`, `.max`)",
        "B": "`torch.float_limits(torch.float16)` and `torch.int_limits(torch.int16)`",
        "C": "`torch.float16.max_value()` and `torch.int16.max_value()`",
        "D": "`torch.limits(torch.float16)` for both floating-point and integer types"
    },
    ["A"],
    "`torch.finfo(dtype)` returns an object containing machine limits for floating-point types (`.bits`, `.eps`, `.max`, `.min`, `.tiny`, `.resolution`), and `torch.iinfo(dtype)` returns machine limits for integer types (`.bits`, `.max`, `.min`).",
    {
        "A": "Correct. `torch.finfo` and `torch.iinfo` provide numerical properties for floating-point and integer dtypes respectively.",
        "B": "Incorrect. `torch.float_limits` and `torch.int_limits` do not exist in PyTorch.",
        "C": "Incorrect. `torch.dtype` objects do not have a `.max_value()` method.",
        "D": "Incorrect. `torch.limits` does not exist; PyTorch follows the `finfo`/`iinfo` convention."
    },
    "Query dtype numerical bounds and machine epsilon with torch.finfo and torch.iinfo",
    "PyTorch Docs: torch.finfo and torch.iinfo"
)

add_q(
    "PTCA-F-054", A2, "Hard", False,
    "What happens in PyTorch's type promotion rules when a 1D tensor of `dtype=torch.int8` is multiplied by a Python `float` scalar `2.5` (`x * 2.5`) versus multiplied by a 0D `float64` tensor `torch.tensor(2.5, dtype=torch.float64)`?",
    "import torch\n\nx = torch.tensor([1, 2, 3], dtype=torch.int8)\nr1 = x * 2.5\nr2 = x * torch.tensor(2.5, dtype=torch.float64)\nprint(r1.dtype, r2.dtype)",
    {
        "A": "torch.float32 torch.float64",
        "B": "torch.float64 torch.float64",
        "C": "torch.int8 torch.float64",
        "D": "torch.float16 torch.float32"
    },
    ["A"],
    "Even though a Python `float` (`2.5`) is 64-bit in Python, PyTorch treats Python float scalars and 0D wrapped numbers as having the default floating-point type (`torch.float32`) during category promotion with an integer tensor (`x * 2.5` -> `torch.float32`). However, when multiplied by an explicit `torch.float64` tensor, the result promotes to `torch.float64`.",
    {
        "A": "Correct. An integer tensor combined with a Python `float` scalar promotes to `torch.get_default_dtype()` (`torch.float32`), whereas an explicit `torch.float64` tensor promotes the result to `torch.float64`.",
        "B": "Incorrect. PyTorch intentionally avoids promoting tensors to `float64` when combined with Python `float` literals so that `x * 2.5` stays in fast `float32` precision.",
        "C": "Incorrect. Multiplying an integer tensor by `2.5` promotes the category from `int` to `float` (`torch.float32`).",
        "D": "Incorrect. Default float promotion uses `torch.float32`, not `torch.float16`."
    },
    "Distinguish Python scalar type promotion from explicit Tensor dtype promotion",
    "PyTorch Docs: Type Promotion Documentation"
)

print(f"Loaded {len(questions)} total questions after A2.")

A3 = "A3: Indexing, Slicing, Reshaping, Views & Copies"

add_q(
    "PTCA-F-055", A3, "Easy", False,
    "What is the output of the following code comparing Python variable assignment `b = a` and `c = a.clone()`?",
    "import torch\n\na = torch.ones(2, 2)\nb = a\nc = a.clone()\n\na[0, 1] = 561\nprint(int(b[0, 1]), int(c[0, 1]))",
    {
        "A": "561 1",
        "B": "561 561",
        "C": "1 1",
        "D": "1 561"
    },
    ["A"],
    "As shown in Module 2 (`1_tensor_basic.ipynb`), assigning `b = a` only binds a new Python variable label to the exact same underlying `Tensor` object, so modifying `a[0, 1] = 561` is reflected in `b[0, 1]`. Calling `c = a.clone()` allocates a separate copy of the tensor's memory storage, so `c[0, 1]` remains `1.0`.",
    {
        "A": "Correct. `b` references the same tensor (`561`), whereas `c` is an independent `.clone()` (`1`).",
        "B": "Incorrect. `a.clone()` allocates distinct storage so `c` is unaffected by subsequent in-place changes to `a`.",
        "C": "Incorrect. `b = a` does not copy the tensor in Python; `b` and `a` point to the same object.",
        "D": "Incorrect. `b` changes to `561` while `c` stays `1`."
    },
    "Distinguish Python reference assignment from memory copying via .clone()",
    "modules/module_2_tensors/1_tensor_basic.ipynb"
)

add_q(
    "PTCA-F-056", A3, "Hard", False,
    "Consider a tensor `x` with `requires_grad=True` and `z = x * 2`. Compare `z_clone = z.clone()`, `z_det = z.detach()`, and `z_both = z.clone().detach()` in terms of (1) sharing storage with `z` and (2) tracking autograd history (`requires_grad`). Which statement is completely accurate?",
    "import torch\n\nx = torch.tensor([1.0, 2.0], requires_grad=True)\nz = x * 2\nz_clone = z.clone()\nz_det = z.detach()\nz_both = z.clone().detach()",
    {
        "A": "`z_clone` allocates new storage AND stays connected to the autograd graph (`grad_fn=<CloneBackward0>`); `z_det` shares storage with `z` (`requires_grad=False`); `z_both` allocates new storage AND is detached from the autograd graph (`requires_grad=False`).",
        "B": "`z_clone` detaches the tensor from autograd (`requires_grad=False`), while `z_det` allocates a new memory copy.",
        "C": "Both `z_clone` and `z_det` allocate new memory copies and set `requires_grad=False`.",
        "D": "`z_det` keeps `requires_grad=True` while `z_clone` shares the same underlying memory buffer with `z`."
    },
    ["A"],
    "`.clone()` creates a new memory copy but is recorded as a differentiable operation in autograd (`z_clone.requires_grad` is `True` and gradients flow back through `CloneBackward0` to `x`). `.detach()` returns a view that shares the same storage as `z` (`z_det.untyped_storage().data_ptr() == z.untyped_storage().data_ptr()`), with computation history forgotten (`requires_grad=False`, `grad_fn=None`). Combining `.clone().detach()` (or `.detach().clone()`) yields both independent memory storage AND no autograd history.",
    {
        "A": "Correct. `.clone()` copies memory and preserves autograd history; `.detach()` shares memory and drops autograd history; `.clone().detach()` copies memory and drops autograd history.",
        "B": "Incorrect. This reverses `.clone()` and `.detach()`.",
        "C": "Incorrect. `.clone()` keeps `requires_grad=True`, and `.detach()` shares memory with `z` rather than copying.",
        "D": "Incorrect. `.detach()` always sets `requires_grad=False`, and `.clone()` always allocates new memory."
    },
    "Contrast memory sharing and autograd tracking across .clone(), .detach(), and .clone().detach()",
    "modules/module_2_tensors/1_tensor_basic.ipynb & 3_tensor_operations.ipynb"
)

add_q(
    "PTCA-F-057", A3, "Medium", False,
    "What is the output of the following code comparing basic slicing (`x[0:2]`) with advanced integer list indexing (`x[[0, 1]]`) when the resulting tensors are modified in-place?",
    "import torch\n\nx = torch.tensor([10, 20, 30, 40])\ny = torch.tensor([10, 20, 30, 40])\n\ns = x[0:2]      # basic slice\nf = y[[0, 1]]   # advanced/fancy indexing\n\ns[0] = 999\nf[0] = 999\nprint(int(x[0]), int(y[0]))",
    {
        "A": "999 10",
        "B": "999 999",
        "C": "10 10",
        "D": "10 999"
    },
    ["A"],
    "Basic slicing (`x[start:stop:step]`) always returns a **view** sharing storage with `x`, so setting `s[0] = 999` mutates `x[0]` to `999`. Advanced (fancy) indexing using a list or tensor of indices (`y[[0, 1]]`) returns a **copy** in new memory when accessed as an rvalue, so mutating `f[0] = 999` does NOT modify `y[0]`.",
    {
        "A": "Correct. Basic slicing returns a view (`x[0]` becomes `999`), whereas fancy indexing returns a copy (`y[0]` remains `10`).",
        "B": "Incorrect. Fancy indexing (`y[[0, 1]]`) cannot be represented by constant strides in general, so it returns a new copy.",
        "C": "Incorrect. Basic slicing (`x[0:2]`) shares storage with `x`.",
        "D": "Incorrect. `x[0]` is modified via the slice view, whereas `y[0]` is not modified."
    },
    "Distinguish view semantics of basic slicing from copy semantics of advanced indexing",
    "PyTorch Docs: Tensor Views and Indexing"
)

add_q(
    "PTCA-F-058", A3, "Medium", False,
    "Given a 3D tensor `x = torch.zeros(4, 5, 6)`, what are the shapes of `x[1, :, :]` (integer index on dim 0) versus `x[1:2, :, :]` (length-1 slice on dim 0)?",
    "import torch\nx = torch.zeros(4, 5, 6)\na = x[1, :, :]\nb = x[1:2, :, :]\nprint(a.shape, b.shape)",
    {
        "A": "torch.Size([5, 6]) torch.Size([1, 5, 6])",
        "B": "torch.Size([1, 5, 6]) torch.Size([1, 5, 6])",
        "C": "torch.Size([5, 6]) torch.Size([5, 6])",
        "D": "torch.Size([4, 5]) torch.Size([1, 5, 6])"
    },
    ["A"],
    "Indexing an axis with a scalar integer (`1`) selects that hyperplane and reduces the tensor's rank by 1 (`(5, 6)`). Indexing with a slice (`1:2`) preserves the tensor's rank (`ndim == 3`) with size `1` along that axis (`(1, 5, 6)`). Both `a` and `b` are views of `x`.",
    {
        "A": "Correct. Integer indexing drops the indexed dimension (`(5, 6)`), whereas slicing preserves the dimension (`(1, 5, 6)`).",
        "B": "Incorrect. Integer indexing `x[1, :, :]` squeezes out dimension 0.",
        "C": "Incorrect. Slicing `x[1:2, :, :]` retains dimension 0 with length 1.",
        "D": "Incorrect. Dimension 0 was indexed, leaving dimensions 1 and 2 of sizes `5` and `6`."
    },
    "Contrast rank reduction under integer indexing with rank preservation under slicing",
    "PyTorch Docs: Tensor Indexing"
)

add_q(
    "PTCA-F-059", A3, "Medium", False,
    "What is the shape and content of the output when a 2D tensor is indexed with a 2D boolean mask `x[x > 2]`?",
    "import torch\n\nx = torch.tensor([[1, 4, 2],\n                  [5, 0, 3]])\nout = x[x > 2]\nprint(out.shape, out.tolist())",
    {
        "A": "torch.Size([3]) [4, 5, 3]",
        "B": "torch.Size([2, 3]) [[0, 4, 0], [5, 0, 3]]",
        "C": "torch.Size([2, 2]) [[4, 2], [5, 3]]",
        "D": "torch.Size([3, 2]) [[0, 1], [1, 0], [1, 2]]"
    },
    ["A"],
    "Indexing an $N$-dimensional tensor with an $N$-dimensional boolean mask always returns a **1D tensor** (a copy) containing the matching elements in row-major order (`[4, 5, 3]`, shape `torch.Size([3])`), because the number of `True` entries per row can vary.",
    {
        "A": "Correct. Boolean mask indexing flattens the selected elements into a 1D tensor `[4, 5, 3]` of shape `(3,)`.",
        "B": "Incorrect. Zeroing out non-matching elements while preserving 2D shape `(2, 3)` requires `torch.where(x > 2, x, 0)` or `x * (x > 2)`.",
        "C": "Incorrect. Only 3 elements are strictly greater than 2 (`4, 5, 3`), so the result cannot be `(2, 2)`.",
        "D": "Incorrect. `[[0, 1], [1, 0], [1, 2]]` is the output of `torch.nonzero(x > 2)` (indices), not `x[x > 2]` (values)."
    },
    "Apply boolean mask indexing and predict 1D output shape",
    "PyTorch Docs: Tensor Indexing"
)

add_q(
    "PTCA-F-060", A3, "Easy", False,
    "A developer wants to replace all negative values in a 2D tensor `x` with `0.0` and double all non-negative values (`x * 2.0`), while preserving the original shape of `x`. Which `torch.where` call accomplishes this?",
    "import torch\nx = torch.tensor([[-1.0, 2.0], [3.0, -4.0]])\n# Replace x < 0 with 0.0 and x >= 0 with x * 2.0",
    {
        "A": "torch.where(x >= 0, x * 2.0, 0.0)",
        "B": "torch.where(x >= 0, 0.0, x * 2.0)",
        "C": "x[x >= 0] * 2.0",
        "D": "torch.nonzero(x >= 0, x * 2.0, 0.0)"
    },
    ["A"],
    "`torch.where(condition, input, other)` returns a tensor of elements selected from `input` where `condition` is `True` and from `other` where `condition` is `False` (supporting scalar broadcasting for `input` and `other`).",
    {
        "A": "Correct. Where `x >= 0` is `True`, it selects `x * 2.0`; where `False`, it selects `0.0`.",
        "B": "Incorrect. The second and third arguments are reversed (`input` is for `True`, `other` is for `False`).",
        "C": "Incorrect. Boolean indexing `x[x >= 0]` drops negative entries and returns a 1D tensor rather than preserving the `(2, 2)` shape.",
        "D": "Incorrect. `torch.nonzero` only finds coordinates of non-zero elements and does not accept `input`/`other` replacement arguments."
    },
    "Perform conditional element-wise selection using torch.where",
    "PyTorch Docs: torch.where"
)

add_q(
    "PTCA-F-061", A3, "Medium", False,
    "What is the difference between `torch.nonzero(x)` (default `as_tuple=False`) and `torch.nonzero(x, as_tuple=True)` (or `torch.where(x != 0)`) on a 2D tensor `x` with 3 non-zero elements?",
    "import torch\n\nx = torch.tensor([[0, 5, 0],\n                  [7, 0, 9]])\nnz_mat = torch.nonzero(x)\nnz_tup = torch.nonzero(x, as_tuple=True)\nprint(nz_mat.shape, len(nz_tup), nz_tup[0].shape)",
    {
        "A": "torch.Size([3, 2]) 2 torch.Size([3])",
        "B": "torch.Size([2, 3]) 3 torch.Size([2])",
        "C": "torch.Size([3]) 2 torch.Size([3, 2])",
        "D": "torch.Size([3, 2]) 3 torch.Size([2])"
    },
    ["A"],
    "By default (`as_tuple=False`), `torch.nonzero(x)` returns a 2D tensor of shape `(num_nonzero, x.ndim)` = `(3, 2)`, where each row is the `(row_idx, col_idx)` coordinate of a non-zero element. When `as_tuple=True`, it returns a tuple of `x.ndim` (`2`) 1D index tensors, each of length `num_nonzero` (`torch.Size([3])`), suitable for direct advanced indexing `x[nz_tup]`.",
    {
        "A": "Correct. `nz_mat` has shape `(3, 2)` (3 non-zero items, 2 coordinates each), and `nz_tup` is a 2-tuple of 1D tensors of shape `(3,)`.",
        "B": "Incorrect. `nz_mat` has shape `(z, ndim) = (3, 2)`, not `(2, 3)`, and `len(nz_tup)` equals `x.ndim = 2`.",
        "C": "Incorrect. `nz_mat` is 2D of shape `(3, 2)`.",
        "D": "Incorrect. `nz_tup` has one 1D tensor per dimension of `x` (`len(nz_tup) == x.ndim == 2`), each of length `3`."
    },
    "Extract non-zero coordinates with torch.nonzero in both matrix and tuple modes",
    "PyTorch Docs: torch.nonzero"
)

add_q(
    "PTCA-F-062", A3, "Medium", False,
    "Why does `x.transpose(0, 1).view(-1)` raise a `RuntimeError` in the code below, while `x.transpose(0, 1).reshape(-1)` succeeds?",
    "import torch\n\nx = torch.arange(6).view(2, 3)\nt = x.transpose(0, 1)\n# t.view(-1) -> RuntimeError!\nr = t.reshape(-1)",
    {
        "A": "`t` is non-contiguous (`t.stride() == (1, 3)`), and `.view()` strictly requires the tensor's memory strides to be compatible with the new shape without copying, whereas `.reshape()` returns a view when possible and automatically copies to contiguous memory when necessary.",
        "B": "`.view()` cannot accept `-1` as a dimension argument, whereas `.reshape()` supports `-1`.",
        "C": "`.view()` only works on 1D tensors, whereas `.reshape()` works on 2D tensors.",
        "D": "`x.transpose(0, 1)` changes the number of elements in `t`, invalidating `.view()`."
    },
    ["A"],
    "Transposing a `(2, 3)` tensor with strides `(3, 1)` produces a `(3, 2)` view with strides `(1, 3)`, which is not C-contiguous (`t.is_contiguous() == False`). Flattening a `(3, 2)` tensor with strides `(1, 3)` into a 1D tensor of 6 elements cannot be represented by a single constant stride without rearranging memory. `.view(-1)` never copies data and therefore raises `RuntimeError: view size is not compatible with input tensor's size and stride`, whereas `.reshape(-1)` falls back to `t.contiguous().view(-1)`.",
    {
        "A": "Correct. `.view()` guarantees zero-copy view creation and fails on incompatible non-contiguous strides, while `.reshape()` copies when needed.",
        "B": "Incorrect. Both `.view()` and `.reshape()` support `-1` for automatic single-dimension inference.",
        "C": "Incorrect. `.view()` works on any contiguous tensor of any rank.",
        "D": "Incorrect. Transposition preserves `numel() == 6`."
    },
    "Distinguish .view() contiguity requirements from .reshape() fallback behavior",
    "PyTorch Docs: Tensor Views, torch.Tensor.view, and torch.Tensor.reshape"
)

add_q(
    "PTCA-F-063", A3, "Easy", False,
    "A tensor `x` has shape `(8, 3, 16, 16)`. You call `y = x.view(8, -1, 64)`. What is the resulting shape of `y`, and what happens if you instead call `x.view(8, -1, -1)`?",
    "import torch\nx = torch.empty(8, 3, 16, 16)\ny = x.view(8, -1, 64)",
    {
        "A": "`y.shape` is `torch.Size([8, 12, 64])`; calling `x.view(8, -1, -1)` raises a `RuntimeError: only one dimension can be inferred`.",
        "B": "`y.shape` is `torch.Size([8, 48, 64])`; calling `x.view(8, -1, -1)` evenly splits the remaining size into `(8, 28, 28)`.",
        "C": "`y.shape` is `torch.Size([8, 12, 64])`; calling `x.view(8, -1, -1)` sets the last two dimensions to `1`.",
        "D": "`y.shape` raises a `RuntimeError` because `3 * 16 * 16` is not divisible by `64`."
    },
    ["A"],
    "The total number of elements is $8 \\times 3 \\times 16 \\times 16 = 6144$. Since $3 \\times 16 \\times 16 = 768$ and $768 / 64 = 12$, the inferred dimension `-1` resolves to `12`, giving `torch.Size([8, 12, 64])`. At most ONE dimension can be specified as `-1`; passing two `-1`s is ambiguous and raises `RuntimeError: only one dimension can be inferred`.",
    {
        "A": "Correct. $768 / 64 = 12$ gives `(8, 12, 64)`, and specifying more than one `-1` raises a `RuntimeError`.",
        "B": "Incorrect. $48 \\times 64 = 3072 \\neq 768$, and multiple `-1` dimensions are never allowed.",
        "C": "Incorrect. `-1` infers the missing factor from `numel()`, and cannot appear more than once.",
        "D": "Incorrect. $3 \\times 16 \\times 16 = 768 = 12 \\times 64$, which is evenly divisible by 64."
    },
    "Use -1 dimension inference in .view() and .reshape()",
    "PyTorch Docs: torch.Tensor.view"
)

add_q(
    "PTCA-F-064", A3, "Medium", False,
    "What is the output of the following code inspecting `.is_contiguous()`, `.stride()`, and `.contiguous()` after a transpose operation?",
    "import torch\n\nx = torch.arange(12).view(3, 4)\nt = x.transpose(0, 1)\nc = t.contiguous()\nprint(x.is_contiguous(), t.is_contiguous(), c.is_contiguous(), t.stride(), c.stride())",
    {
        "A": "True False True (1, 4) (4, 1)",
        "B": "True False True (1, 4) (3, 1)",
        "C": "True True True (3, 1) (3, 1)",
        "D": "True False False (4, 1) (1, 3)"
    },
    ["B"],
    "`x` has shape `(3, 4)` and contiguous row-major strides `(4, 1)` (`x.is_contiguous() == True`). `t = x.transpose(0, 1)` swaps both the shape to `(4, 3)` and the strides to `(1, 4)`, making `t.is_contiguous() == False`. Calling `c = t.contiguous()` allocates a new contiguous tensor of shape `(4, 3)` whose row-major strides are `(3, 1)` (`c.is_contiguous() == True`).",
    {
        "A": "Incorrect. Since `t` and `c` have shape `(4, 3)` (4 rows, 3 columns), the contiguous stride along dim 0 is `3` (`(3, 1)`), not `4` (`(4, 1)`).",
        "B": "Correct. `x` is contiguous, `t` is non-contiguous with strides `(1, 4)`, and `c` is contiguous of shape `(4, 3)` with strides `(3, 1)`.",
        "C": "Incorrect. Transposing a 2D matrix with both dimensions > 1 makes it non-contiguous (`t.is_contiguous() == False`).",
        "D": "Incorrect. `c = t.contiguous()` guarantees `c.is_contiguous() == True` with strides `(3, 1)`."
    },
    "Track contiguity and stride changes across .transpose() and .contiguous()",
    "PyTorch Docs: torch.Tensor.is_contiguous and torch.Tensor.contiguous"
)

add_q(
    "PTCA-F-065", A3, "Medium", False,
    "How do `x.transpose(dim0, dim1)`, `x.permute(*dims)`, and `x.T` differ when working with a 4D batch of images `x` of shape `(B, H, W, C)`?",
    "import torch\nx = torch.empty(16, 224, 224, 3) # (B, H, W, C)",
    {
        "A": "`x.transpose(dim0, dim1)` swaps exactly two dimensions at a time; `x.permute(0, 3, 1, 2)` reorders all dimensions simultaneously in a single call; and using `x.T` on a tensor with `ndim > 2` is deprecated/discouraged (reversing all dimensions to `(3, 224, 224, 16)`).",
        "B": "`x.transpose(0, 3, 1, 2)` and `x.permute(0, 3, 1, 2)` have identical signatures in PyTorch.",
        "C": "`x.permute(0, 3, 1, 2)` always copies the underlying memory buffer, while `x.transpose` returns a view.",
        "D": "`x.T` swaps only the last two dimensions `(B, H, C, W)` like `x.mT`."
    },
    ["A"],
    "Unlike NumPy's `np.transpose(a, axes=(0, 3, 1, 2))`, PyTorch's `torch.transpose(input, dim0, dim1)` only accepts two dimension indices to swap. To reorder multiple axes at once (such as `(B, H, W, C) -> (B, C, H, W)`), use `x.permute(0, 3, 1, 2)`. Both `transpose` and `permute` return zero-copy views. Also, `x.T` on `ndim > 2` emits a warning in PyTorch (use `x.mT` to transpose the last two matrix dimensions, or `x.permute(...)`).",
    {
        "A": "Correct. `transpose` swaps two axes, `permute` reorders all axes in one call, and `x.T` is only intended for 2D matrices.",
        "B": "Incorrect. Passing 4 dimension indices to `x.transpose(0, 3, 1, 2)` raises a `TypeError` in PyTorch.",
        "C": "Incorrect. Both `x.permute()` and `x.transpose()` return strided views without copying memory.",
        "D": "Incorrect. Swapping the last two dimensions of a batched tensor is `x.mT` (or `x.transpose(-2, -1)`), not `x.T`."
    },
    "Compare .transpose(), .permute(), .T, and .mT on multi-dimensional tensors",
    "PyTorch Docs: torch.transpose and torch.permute"
)

add_q(
    "PTCA-F-066", A3, "Easy", False,
    "An image loaded from OpenCV/NumPy has shape `(H, W, C) = (480, 640, 3)`. Standard PyTorch 2D convolutional layers (`nn.Conv2d`) expect channel-first layout `(C, H, W) = (3, 480, 640)`. Why is `img.permute(2, 0, 1)` correct while `img.view(3, 480, 640)` is a bug?",
    "import torch\nimg = torch.randint(0, 256, (480, 640, 3), dtype=torch.uint8)",
    {
        "A": "`img.permute(2, 0, 1)` properly re-indexes the strides so channel `c` at `(h, w)` maps to `[c, h, w]`, whereas `img.view(3, 480, 640)` keeps the interleaved `R,G,B,R,G,B...` memory order unchanged and scrambles spatial pixels across the 3 channels.",
        "B": "`img.view(3, 480, 640)` raises a `RuntimeError` because `480 * 640 * 3` does not match `3 * 480 * 640`.",
        "C": "`img.permute(2, 0, 1)` normalizes the pixel values from `[0, 255]` to `[0.0, 1.0]` automatically.",
        "D": "`img.view(3, 480, 640)` only works on float tensors, not `uint8` tensors."
    },
    ["A"],
    "In an `(H, W, C)` tensor, each pixel's `(R, G, B)` values are adjacent in memory. Calling `.view(3, 480, 640)` does not transpose axes; it simply slices the flat buffer into three consecutive chunks (top third of image, middle third, bottom third) with interleaved RGB stripes, corrupting the image spatial structure without raising any error (`numel` is identical). `img.permute(2, 0, 1)` changes the axis order and strides `(1, 1920, 3)` so `[c, h, w]` accesses the true channel `c` at row `h`, col `w`.",
    {
        "A": "Correct. `.permute(2, 0, 1)` transposes axes properly, while `.view(3, 480, 640)` silently scrambles spatial and channel data.",
        "B": "Incorrect. Because `3 * 480 * 640 == 480 * 640 * 3` and `img` is contiguous, `.view(3, 480, 640)` runs without raising any error, making it a silent bug!",
        "C": "Incorrect. `.permute()` only changes shape and strides; it never modifies or scales element values.",
        "D": "Incorrect. `.view()` works on contiguous tensors of any dtype."
    },
    "Convert HWC image tensors to CHW using .permute(2, 0, 1) instead of .view()",
    "PyTorch Docs: torch.Tensor.permute"
)

add_q(
    "PTCA-F-067", A3, "Medium", False,
    "A model outputs predictions of shape `(B, 1, 10)` where `B` is the batch size and `1` is a singleton channel dimension. Why is calling `out = preds.squeeze()` dangerous in a production inference loop, and what should be used instead?",
    "import torch\n\n# Case 1: full batch of 32 samples\npreds_32 = torch.randn(32, 1, 10)\n# Case 2: last batch of dataset has only 1 sample\npreds_1 = torch.randn(1, 1, 10)\n\nprint(preds_32.squeeze().shape, preds_1.squeeze().shape, preds_1.squeeze(dim=1).shape)",
    {
        "A": "When `B == 1` (e.g., single-sample inference or the final remainder batch of a `DataLoader`), `preds.squeeze()` removes BOTH the batch dimension `0` and channel dimension `1`, collapsing the shape from `(1, 1, 10)` to `(10,)` instead of `(1, 10)`; passing `preds.squeeze(dim=1)` safely removes only axis `1`.",
        "B": "`preds.squeeze()` without arguments raises a `RuntimeError` whenever a tensor has more than one singleton dimension.",
        "C": "`preds.squeeze()` copies the entire tensor in memory, whereas `preds.squeeze(dim=1)` returns a view.",
        "D": "`preds.squeeze(dim=1)` raises an error if dimension `1` has size `1`."
    },
    ["A"],
    "Calling `.squeeze()` with no `dim` argument strips **every** dimension of size `1`. When batch size `B` happens to be `1`, `preds_1.squeeze()` removes `dim=0` as well as `dim=1`, changing the tensor rank from 2D `(B, 10)` to 1D `(10,)` and breaking downstream batch code. Specifying `preds.squeeze(dim=1)` (or `preds.squeeze(1)`) only removes dimension `1`.",
    {
        "A": "Correct. Unconditional `.squeeze()` causes the classic batch-size-1 rank bug (`(10,)` instead of `(1, 10)`); `.squeeze(dim=1)` targets only axis `1`.",
        "B": "Incorrect. `.squeeze()` removes all singleton dimensions without raising an error (and in recent PyTorch versions can even take a tuple of dims `dim=(1,)`).",
        "C": "Incorrect. Both `.squeeze()` and `.squeeze(dim=1)` return zero-copy views.",
        "D": "Incorrect. If the specified `dim` has size `1`, `.squeeze(dim)` removes it; if the specified `dim` has size `> 1`, `.squeeze(dim)` is a safe no-op returning the tensor unchanged."
    },
    "Prevent batch-size-1 rank collapse by specifying dim in .squeeze(dim)",
    "PyTorch Docs: torch.squeeze"
)

add_q(
    "PTCA-F-068", A3, "Easy", False,
    "What happens when you call `x.squeeze(dim=0)` on a tensor `x` of shape `(4, 1, 8)` where dimension `0` has size `4` (not `1`)?",
    "import torch\nx = torch.empty(4, 1, 8)\ny = x.squeeze(dim=0)\nprint(y.shape)",
    {
        "A": "It returns a view of `x` with its shape unchanged (`torch.Size([4, 1, 8])`), without raising an error.",
        "B": "It raises a `ValueError: cannot select an axis to squeeze out which has size not equal to one` (like NumPy).",
        "C": "It squeezes dimension `1` instead, returning `torch.Size([4, 8])`.",
        "D": "It takes the first slice `x[0]` and returns `torch.Size([1, 8])`."
    },
    ["A"],
    "Unlike NumPy (which raises a `ValueError` when squeezing a non-singleton axis), PyTorch's `x.squeeze(dim)` is a no-op if `x.size(dim) != 1`, returning a view of `x` with the original shape `(4, 1, 8)`.",
    {
        "A": "Correct. In PyTorch, `squeeze(dim)` leaves the tensor shape unchanged if `x.size(dim) != 1`.",
        "B": "Incorrect. NumPy raises `ValueError`, but PyTorch returns the tensor unchanged.",
        "C": "Incorrect. When `dim=0` is explicitly passed, PyTorch only checks dimension `0` and leaves dimension `1` untouched.",
        "D": "Incorrect. `squeeze` never drops elements or slices into non-singleton dimensions."
    },
    "Understand PyTorch's no-op behavior when calling .squeeze(dim) on non-singleton dimensions",
    "PyTorch Docs: torch.squeeze"
)

add_q(
    "PTCA-F-069", A3, "Easy", True,
    "Given a single 3-channel image tensor `img` of shape `(3, 224, 224)`, which TWO expressions produce a 4D batch tensor of shape `(1, 3, 224, 224)` as a view?",
    "import torch\nimg = torch.empty(3, 224, 224)",
    {
        "A": "img.unsqueeze(0)",
        "B": "img[None, ...]",
        "C": "img.unsqueeze(-1)",
        "D": "img.squeeze(0)"
    },
    ["A", "B"],
    "`img.unsqueeze(0)` inserts a new singleton dimension of size `1` at dimension index `0`, producing `(1, 3, 224, 224)`. Indexing with `None` (an alias for `torch.newaxis`) at position 0 (`img[None, ...]` or `img[None]`) is equivalent to `img.unsqueeze(0)`.",
    {
        "A": "Correct. `img.unsqueeze(0)` inserts a size-1 dimension at axis 0, yielding `(1, 3, 224, 224)`.",
        "B": "Correct. Indexing with `None` inserts a new axis of length 1 at that position (`(1, 3, 224, 224)`).",
        "C": "Incorrect. `img.unsqueeze(-1)` inserts the singleton dimension at the end, yielding `(3, 224, 224, 1)`.",
        "D": "Incorrect. `img.squeeze(0)` removes a singleton dimension (or is a no-op here since dim 0 is size 3)."
    },
    "Insert singleton batch dimensions using .unsqueeze() and None indexing",
    "PyTorch Docs: torch.unsqueeze"
)

add_q(
    "PTCA-F-070", A3, "Medium", False,
    "A convolutional feature map `feat` has shape `(32, 64, 7, 7)` representing `(batch_size, channels, height, width)`. To pass `feat` into a fully connected `nn.Linear(64 * 7 * 7, 10)` layer while preserving the batch dimension `0`, what is the difference between `torch.flatten(feat)` and `torch.flatten(feat, start_dim=1)`?",
    "import torch\n\nfeat = torch.empty(32, 64, 7, 7)\nf_all = torch.flatten(feat)\nf_batch = torch.flatten(feat, start_dim=1)\nprint(f_all.shape, f_batch.shape)",
    {
        "A": "torch.Size([100352]) torch.Size([32, 3136])",
        "B": "torch.Size([32, 3136]) torch.Size([32, 64, 49])",
        "C": "torch.Size([100352]) torch.Size([3136, 32])",
        "D": "torch.Size([32, 3136]) torch.Size([32, 3136])"
    },
    ["A"],
    "`torch.flatten(input, start_dim=0, end_dim=-1)` defaults to `start_dim=0`, which collapses **all** dimensions (including the batch dimension) into a single 1D vector of length $32 \\times 64 \\times 7 \\times 7 = 100352$. Passing `start_dim=1` (or using `nn.Flatten()` which defaults to `start_dim=1`) preserves dimension `0` (`32`) and flattens dimensions `1..3` into $64 \\times 7 \\times 7 = 3136$.",
    {
        "A": "Correct. `torch.flatten(feat)` defaults to `start_dim=0` (`(100352,)`), whereas `torch.flatten(feat, start_dim=1)` preserves the batch axis (`(32, 3136)`).",
        "B": "Incorrect. `torch.flatten` functional API defaults to `start_dim=0` (unlike `nn.Flatten` module which defaults to `start_dim=1`).",
        "C": "Incorrect. `start_dim=1` keeps the batch dimension `32` as axis 0 (`(32, 3136)`).",
        "D": "Incorrect. Omitting `start_dim=1` in `torch.flatten(feat)` collapses the batch dimension into a 1D tensor."
    },
    "Flatten spatial feature maps while preserving the batch dimension via torch.flatten(x, start_dim=1)",
    "PyTorch Docs: torch.flatten"
)

add_q(
    "PTCA-F-071", A3, "Easy", False,
    "Given two tensors `a = torch.zeros(2, 3)` and `b = torch.ones(2, 3)`, what are the shapes of `torch.cat([a, b], dim=0)`, `torch.cat([a, b], dim=1)`, and `torch.stack([a, b], dim=0)`?",
    "import torch\n\na = torch.zeros(2, 3)\nb = torch.ones(2, 3)\nc0 = torch.cat([a, b], dim=0)\nc1 = torch.cat([a, b], dim=1)\ns0 = torch.stack([a, b], dim=0)\nprint(c0.shape, c1.shape, s0.shape)",
    {
        "A": "torch.Size([4, 3]) torch.Size([2, 6]) torch.Size([2, 2, 3])",
        "B": "torch.Size([2, 2, 3]) torch.Size([2, 3, 2]) torch.Size([4, 3])",
        "C": "torch.Size([4, 6]) torch.Size([4, 6]) torch.Size([2, 2, 3])",
        "D": "torch.Size([4, 3]) torch.Size([2, 6]) torch.Size([4, 3])"
    },
    ["A"],
    "`torch.cat` concatenates tensors along an **existing** dimension (preserving rank `ndim == 2`): along `dim=0` the size becomes `(2 + 2, 3) = (4, 3)`, and along `dim=1` it becomes `(2, 3 + 3) = (2, 6)`. `torch.stack` joins identically shaped tensors along a **new** dimension (increasing rank to `ndim == 3`), yielding `(2, 2, 3)` for `dim=0`.",
    {
        "A": "Correct. `cat` adds sizes along the existing dimension (`(4, 3)` and `(2, 6)`), while `stack` inserts a new dimension (`(2, 2, 3)`).",
        "B": "Incorrect. `cat` preserves rank (2D) while `stack` increases rank (3D).",
        "C": "Incorrect. `cat` only sums the dimension sizes along the specified `dim`; non-concatenated dimensions must match and stay unchanged.",
        "D": "Incorrect. `torch.stack` always creates a new dimension (`(2, 2, 3)`), unlike `torch.cat`."
    },
    "Contrast rank-preserving concatenation (torch.cat) with rank-increasing stacking (torch.stack)",
    "PyTorch Docs: torch.cat and torch.stack"
)

add_q(
    "PTCA-F-072", A3, "Medium", False,
    "When does `torch.cat([a, b], dim=1)` succeed while `torch.stack([a, b], dim=1)` raises a `RuntimeError`?",
    "import torch\n\na = torch.empty(4, 3)\nb = torch.empty(4, 5)\n# Compare torch.cat([a, b], dim=1) and torch.stack([a, b], dim=1)",
    {
        "A": "`torch.cat([a, b], dim=1)` succeeds (producing shape `(4, 8)`) because `cat` allows the concatenating dimension (`dim=1`) to have different sizes (`3` and `5`) as long as all other dimensions match; `torch.stack([a, b], dim=1)` raises a `RuntimeError` because `stack` requires ALL input tensors to have the exact same shape.",
        "B": "Both `torch.cat` and `torch.stack` raise a `RuntimeError` because `a` and `b` have different shapes.",
        "C": "`torch.stack([a, b], dim=1)` pads `a` to `(4, 5)` and succeeds, whereas `torch.cat` raises a `RuntimeError`.",
        "D": "Both succeed and return shape `(4, 8)`."
    },
    ["A"],
    "`torch.cat` requires non-empty tensors to have the same shape in every dimension *except* the concatenating dimension `dim`. Thus `(4, 3)` and `(4, 5)` concatenate along `dim=1` to `(4, 8)`. `torch.stack` requires every tensor in the sequence to have the **exact** same shape in all dimensions.",
    {
        "A": "Correct. `cat` permits differing sizes along the concatenation axis (`3 + 5 = 8`), whereas `stack` requires identical shapes across all axes.",
        "B": "Incorrect. `torch.cat([a, b], dim=1)` is completely valid when only `dim=1` differs.",
        "C": "Incorrect. `torch.stack` never pads tensors and fails with `RuntimeError: stack expects each tensor to be equal size`.",
        "D": "Incorrect. `torch.stack` fails on `(4, 3)` and `(4, 5)`."
    },
    "Understand shape compatibility rules for torch.cat versus torch.stack",
    "PyTorch Docs: torch.cat and torch.stack"
)

add_q(
    "PTCA-F-073", A3, "Medium", False,
    "A 1D tensor `x = torch.arange(10)` of length `10` is passed to `torch.chunk(x, 3)` and `torch.split(x, 3)`. What are the lengths of the returned sub-tensors in each case?",
    "import torch\n\nx = torch.arange(10)\nchunks = torch.chunk(x, 3)\nsplits = torch.split(x, 3)\nprint([len(t) for t in chunks], [len(t) for t in splits])",
    {
        "A": "[4, 4, 2] [3, 3, 3, 1]",
        "B": "[3, 3, 4] [3, 3, 3, 1]",
        "C": "[3, 3, 3, 1] [4, 4, 2]",
        "D": "[4, 4, 2] [4, 4, 2]"
    },
    ["A"],
    "In `torch.chunk(input, chunks, dim=0)`, the integer `3` specifies the desired **number of chunks**. PyTorch computes chunk size as $\\lceil 10 / 3 \\rceil = 4$, returning 3 views of sizes `[4, 4, 2]`. In `torch.split(tensor, split_size_or_sections, dim=0)`, an integer `3` specifies the **size of each chunk**, returning 4 views of sizes `[3, 3, 3, 1]`.",
    {
        "A": "Correct. `chunk(x, 3)` divides `10` into 3 chunks of size $\\lceil 10/3 \\rceil = 4$ (`[4, 4, 2]`), while `split(x, 3)` splits into chunks of length `3` (`[3, 3, 3, 1]`).",
        "B": "Incorrect. `torch.chunk` puts the smaller remainder chunk at the end (`[4, 4, 2]`), not at the beginning.",
        "C": "Incorrect. This swaps the semantics of `torch.chunk` (number of chunks) and `torch.split` (size of each split).",
        "D": "Incorrect. `torch.split(x, 3)` creates chunks of size 3 (`[3, 3, 3, 1]`)."
    },
    "Distinguish number-of-chunks in torch.chunk from split-size in torch.split",
    "PyTorch Docs: torch.chunk and torch.split"
)

add_q(
    "PTCA-F-074", A3, "Hard", False,
    "What happens when `torch.chunk(torch.arange(10), 6)` is called ( requesting 6 chunks from a 10-element tensor)?",
    "import torch\nx = torch.arange(10)\nc = torch.chunk(x, 6)\nprint(len(c), [len(t) for t in c])",
    {
        "A": "5 [2, 2, 2, 2, 2]",
        "B": "6 [2, 2, 2, 2, 1, 1]",
        "C": "6 [2, 2, 2, 2, 2, 0]",
        "D": "It raises a `RuntimeError` because 10 cannot be divided into 6 non-empty chunks of equal ceiling size."
    },
    ["A"],
    "`torch.chunk(x, chunks)` computes the chunk size as `math.ceil(10 / 6) = 2` and splits the tensor into chunks of size `2`. Because $5 \\times 2 = 10$ exhausts the tensor, `torch.chunk` returns **5** chunks of length 2 (`[2, 2, 2, 2, 2]`) — as noted in the PyTorch docs, `torch.chunk` may return *fewer* than the specified number of chunks! (By contrast, `torch.tensor_split(x, 6)` always returns exactly 6 chunks of sizes `[2, 2, 2, 2, 1, 1]`).",
    {
        "A": "Correct. Because $\\lceil 10 / 6 \\rceil = 2$, `torch.chunk` steps by 2 and returns 5 chunks `[2, 2, 2, 2, 2]`.",
        "B": "Incorrect. Returning `[2, 2, 2, 2, 1, 1]` is the behavior of `torch.tensor_split(x, 6)`, not `torch.chunk(x, 6)`.",
        "C": "Incorrect. `torch.chunk` stops once the 10 elements are consumed and does not append trailing empty chunks here.",
        "D": "Incorrect. `torch.chunk` does not raise an error; it returns fewer chunks than requested."
    },
    "Recognize when torch.chunk returns fewer chunks than requested",
    "PyTorch Docs: torch.chunk"
)

add_q(
    "PTCA-F-075", A3, "Medium", False,
    "You have a tensor `x = torch.empty(64, 14)` and want to split dimension `1` into three uneven feature groups of sizes `3`, `5`, and `6` (`3 + 5 + 6 == 14`). Which call achieves this?",
    "import torch\nx = torch.empty(64, 14)",
    {
        "A": "torch.split(x, [3, 5, 6], dim=1)",
        "B": "torch.chunk(x, [3, 5, 6], dim=1)",
        "C": "torch.split(x, (3, 8, 14), dim=1)",
        "D": "torch.unbind(x, [3, 5, 6], dim=1)"
    },
    ["A"],
    "`torch.split(tensor, split_size_or_sections, dim=0)` accepts either an `int` (uniform chunk size) or a `list`/`tuple` of integers specifying the exact lengths of each section (`[3, 5, 6]`), whose sum must equal `x.size(dim)` (`14`).",
    {
        "A": "Correct. Passing a list of section sizes `[3, 5, 6]` to `torch.split` along `dim=1` returns three views of shapes `(64, 3)`, `(64, 5)`, and `(64, 6)`.",
        "B": "Incorrect. `torch.chunk` only accepts an integer `chunks` argument, not a list of section sizes.",
        "C": "Incorrect. `torch.split` expects section lengths `[3, 5, 6]` summing to `14`, not cumulative split indices `(3, 8, 14)` (cumulative indices are used by `torch.tensor_split`).",
        "D": "Incorrect. `torch.unbind` removes a dimension and returns slices of size 1 along that axis; it does not take section sizes."
    },
    "Split tensors into uneven sections by passing a list of sizes to torch.split",
    "PyTorch Docs: torch.split"
)

add_q(
    "PTCA-F-076", A3, "Hard", False,
    "Compare `x.expand(3, 4)` and `x.repeat(3, 1)` on a 2D row tensor `x = torch.tensor([[1, 2, 3, 4]])` of shape `(1, 4)`. What is printed?",
    "import torch\n\nx = torch.tensor([[1, 2, 3, 4]]) # shape (1, 4)\ne = x.expand(3, 4)\nr = x.repeat(3, 1)\nprint(e.shape, r.shape, e.stride(), r.stride(), e.untyped_storage().nbytes() == x.untyped_storage().nbytes())",
    {
        "A": "torch.Size([3, 4]) torch.Size([3, 4]) (0, 1) (4, 1) True",
        "B": "torch.Size([3, 4]) torch.Size([3, 1, 4]) (4, 1) (4, 1) False",
        "C": "torch.Size([3, 4]) torch.Size([3, 4]) (4, 1) (0, 1) False",
        "D": "torch.Size([3, 16]) torch.Size([3, 4]) (0, 1) (4, 1) True"
    },
    ["A"],
    "`.expand(*sizes)` takes the **target shape** `(3, 4)` and broadcasts singleton dimensions by setting their stride to `0` (`e.stride() == (0, 1)`), creating a zero-copy view sharing the exact same 4-element storage as `x` (`True`). `.repeat(*sizes)` takes the **number of repetitions along each dimension** (`3` times along dim 0, `1` time along dim 1 -> shape `(3, 4)`) and allocates a new contiguous memory copy with strides `(4, 1)`.",
    {
        "A": "Correct. Both have shape `(3, 4)`; `expand` uses a stride-0 view `(0, 1)` sharing `x`'s 4-element storage (`True`), while `repeat` allocates a new contiguous copy `(4, 1)`.",
        "B": "Incorrect. `x.repeat(3, 1)` on a `(1, 4)` tensor multiplies dimensions `(1*3, 4*1) = (3, 4)`, and `e` shares `x`'s storage (`True`).",
        "C": "Incorrect. `expand` sets the broadcasted dimension's stride to `0` (`(0, 1)`), while `repeat` has contiguous strides `(4, 1)`.",
        "D": "Incorrect. `x.expand(3, 4)` sets the final shape to `(3, 4)`, not `(3, 16)`."
    },
    "Contrast zero-copy stride-0 views in .expand() with memory duplication in .repeat()",
    "PyTorch Docs: torch.Tensor.expand and torch.Tensor.repeat"
)

add_q(
    "PTCA-F-077", A3, "Medium", False,
    "What happens if you pass `-1` for a dimension in `x.expand(-1, 4, -1)` on a tensor `x` of shape `(2, 1, 5)`?",
    "import torch\nx = torch.empty(2, 1, 5)\ny = x.expand(-1, 4, -1)\nprint(y.shape)",
    {
        "A": "Passing `-1` in `.expand()` means keeping the existing size of that dimension unchanged, so `y.shape` is `torch.Size([2, 4, 5])`.",
        "B": "It raises a `RuntimeError` because `-1` can only be used once (as in `.view()`).",
        "C": "It flattens the first and last dimensions into a 1D tensor.",
        "D": "It raises a `ValueError` because `.expand()` only accepts positive integers."
    },
    ["A"],
    "In `.expand()`, passing `-1` as the size for any number of dimensions means *do not change the size of that dimension* (keep `x.size(d)`). Thus `x.expand(-1, 4, -1)` keeps `dim=0` (`2`) and `dim=2` (`5`) unchanged while expanding singleton `dim=1` from `1` to `4`, yielding `torch.Size([2, 4, 5])`.",
    {
        "A": "Correct. In `.expand()`, `-1` means 'preserve the original size along this dimension', and can be used on multiple dimensions simultaneously.",
        "B": "Incorrect. Unlike `.view()` where `-1` infers a missing factor and can appear only once, in `.expand()` `-1` simply means 'keep current dimension size' and can appear on any number of axes.",
        "C": "Incorrect. `.expand()` never flattens dimensions.",
        "D": "Incorrect. `-1` is explicitly supported in `.expand()`."
    },
    "Use -1 in .expand() to preserve existing non-singleton dimension sizes",
    "PyTorch Docs: torch.Tensor.expand"
)

add_q(
    "PTCA-F-078", A3, "Medium", False,
    "What does `x.narrow(dim=1, start=2, length=3)` return when called on a tensor `x` of shape `(4, 10)`?",
    "import torch\n\nx = torch.arange(40).view(4, 10)\ny = x.narrow(dim=1, start=2, length=3)\nprint(y.shape, torch.equal(y, x[:, 2:5]), y._base is x)",
    {
        "A": "torch.Size([4, 3]) True True",
        "B": "torch.Size([4, 1]) False True",
        "C": "torch.Size([4, 3]) True False",
        "D": "torch.Size([4, 2]) False False"
    },
    ["A"],
    "`x.narrow(dim, start, length)` returns a narrowed **view** (`y._base is x` is `True`) along dimension `dim` starting at index `start` (`2`) and spanning `length` (`3`) elements—equivalent to slicing `x[:, start : start + length]` (`x[:, 2:5]`), which has shape `(4, 3)`.",
    {
        "A": "Correct. `x.narrow(1, 2, 3)` is a view equivalent to `x[:, 2:2+3]` = `x[:, 2:5]` of shape `(4, 3)`.",
        "B": "Incorrect. The third parameter `3` is `length` (`start + length = 5`), not the exclusive end index `3`.",
        "C": "Incorrect. `narrow` always returns a view sharing storage with `x` (`y._base is x` is `True`).",
        "D": "Incorrect. `length=3` yields size `3` along `dim=1`."
    },
    "Slice tensor dimensions using start and length via .narrow()",
    "PyTorch Docs: torch.narrow"
)

add_q(
    "PTCA-F-079", A3, "Medium", False,
    "What does `torch.unbind(x, dim=1)` return when `x` is a 3D tensor of shape `(2, 4, 5)` (e.g., `(batch, time_steps, features)`)?",
    "import torch\n\nx = torch.empty(2, 4, 5)\nsteps = torch.unbind(x, dim=1)\nprint(type(steps), len(steps), steps[0].shape)",
    {
        "A": "<class 'tuple'> 4 torch.Size([2, 5])",
        "B": "<class 'tuple'> 4 torch.Size([2, 1, 5])",
        "C": "<class 'list'> 2 torch.Size([4, 5])",
        "D": "<class 'torch.Tensor'> 4 torch.Size([2, 5])"
    },
    ["A"],
    "`torch.unbind(input, dim=0)` removes the specified dimension `dim` and returns a `tuple` of all slices along that dimension (each is a view with rank `x.ndim - 1`). For shape `(2, 4, 5)` and `dim=1`, it returns a tuple of `4` tensors, each of shape `(2, 5)` (the exact inverse of `torch.stack(steps, dim=1)`).",
    {
        "A": "Correct. `unbind(x, dim=1)` removes `dim=1` and returns a 4-tuple of `(2, 5)` tensor views.",
        "B": "Incorrect. `unbind` removes the unbound dimension (`(2, 5)`), whereas `torch.chunk(x, 4, dim=1)` or `torch.split(x, 1, dim=1)` keeps the singleton dimension (`(2, 1, 5)`).",
        "C": "Incorrect. `unbind` returns a `tuple`, and since `dim=1` has size `4`, `len(steps)` is `4`.",
        "D": "Incorrect. `unbind` returns a Python `tuple` of tensors, not a single `Tensor`."
    },
    "Decompose a tensor along an axis into a tuple of lower-rank views using torch.unbind",
    "PyTorch Docs: torch.unbind"
)

add_q(
    "PTCA-F-080", A3, "Hard", False,
    "What happens when you index a 2D tensor with two 1D index lists `x[[0, 2], [1, 3]]` versus chaining `x[[0, 2]][:, [1, 3]]`?",
    "import torch\n\nx = torch.arange(12).view(3, 4)\n# [[ 0,  1,  2,  3],\n#  [ 4,  5,  6,  7],\n#  [ 8,  9, 10, 11]]\na = x[[0, 2], [1, 3]]\nb = x[[0, 2]][:, [1, 3]]\nprint(a.shape, a.tolist(), b.shape)",
    {
        "A": "torch.Size([2]) [1, 11] torch.Size([2, 2])",
        "B": "torch.Size([2, 2]) [[1, 3], [9, 11]] torch.Size([2, 2])",
        "C": "torch.Size([2, 4]) [[0, 1, 2, 3], [8, 9, 10, 11]] torch.Size([2])",
        "D": "It raises an `IndexError` because two lists cannot be used simultaneously."
    },
    ["A"],
    "When multiple 1D sequences/tensors of indices are passed together (`x[[0, 2], [1, 3]]`), PyTorch pairs their elements coordinate-wise: `(x[0, 1], x[2, 3]) = (1, 11)` of shape `torch.Size([2])`. To extract the $2 \\times 2$ submatrix at rows `[0, 2]` and columns `[1, 3]`, either slice in two steps `x[[0, 2]][:, [1, 3]]` or broadcast index shapes `x[[[0], [2]], [1, 3]]`, yielding shape `torch.Size([2, 2])`.",
    {
        "A": "Correct. Paired 1D index lists select elements `(0, 1)` and `(2, 3)` (`[1, 11]`, shape `(2,)`), whereas `x[[0, 2]][:, [1, 3]]` selects the `(2, 2)` subgrid.",
        "B": "Incorrect. `x[[0, 2], [1, 3]]` does coordinate-wise zipping, not a Cartesian outer product.",
        "C": "Incorrect. Both row and column indices are applied in `a`.",
        "D": "Incorrect. Multi-axis advanced indexing with equal-length index sequences is valid and broadcasts the index tensors together."
    },
    "Distinguish coordinate-wise paired fancy indexing from rectangular submatrix selection",
    "PyTorch Docs: Tensor Indexing"
)

add_q(
    "PTCA-F-081", A3, "Medium", False,
    "What happens when you attempt to slice a PyTorch tensor with a negative step, such as `x[::-1]`?",
    "import torch\nx = torch.tensor([1, 2, 3, 4])\n# Reverse tensor elements",
    {
        "A": "Calling `x[::-1]` raises `ValueError: step must be greater than zero` because PyTorch strided tensors do not support negative strides; you should use `torch.flip(x, dims=[0])` instead.",
        "B": "Calling `x[::-1]` returns a zero-copy view with `stride == (-1,)` just like NumPy.",
        "C": "Calling `x[::-1]` reverses the tensor in-place and returns `None`.",
        "D": "Calling `x[::-1]` returns an empty tensor `tensor([])`."
    },
    ["A"],
    "Unlike NumPy, PyTorch does not currently support negative strides in `torch.strided` tensors, so slicing with a negative step (`x[::-1]`) raises `ValueError: step must be greater than zero`. To reverse a tensor along one or more dimensions, use `torch.flip(x, dims=[0])` (which returns a copy with reversed elements).",
    {
        "A": "Correct. Negative slice steps raise `ValueError: step must be greater than zero` in PyTorch; `torch.flip(x, dims=[0])` is the standard idiom.",
        "B": "Incorrect. That works in NumPy, and even converting a negative-stride NumPy array `torch.from_numpy(arr[::-1])` raises a `ValueError` in PyTorch unless `.copy()` is called.",
        "C": "Incorrect. Slice notation never mutates a tensor in-place, and negative steps raise `ValueError`.",
        "D": "Incorrect. It raises a `ValueError` rather than returning an empty tensor."
    },
    "Handle negative slice step limitations in PyTorch using torch.flip",
    "PyTorch Docs: torch.flip"
)

add_q(
    "PTCA-F-082", A3, "Medium", False,
    "Although `y = x[[0, 2]]` (fancy indexing on the right-hand side of `=`) returns a copy, what happens when fancy indexing or boolean masking is used on the **left-hand side** of an assignment, such as `x[[0, 2]] = -1` or `x[x < 0] = 0`?",
    "import torch\n\nx = torch.tensor([10, -5, 20, -3])\nx[[0, 2]] = -1\nx[x < 0] = 0\nprint(x.tolist())",
    {
        "A": "[0, 0, 0, 0]",
        "B": "[10, 0, 20, 0]",
        "C": "[-1, -5, -1, -3]",
        "D": "It raises a `RuntimeError` because fancy indexing creates a temporary copy that cannot mutate `x`."
    },
    ["A"],
    "When advanced indexing (`x[[0, 2]] = -1`) or boolean mask indexing (`x[x < 0] = 0`) appears as the target of an assignment (`__setitem__`), Python invokes `x.__setitem__(indices, value)`, which directly mutates `x` in-place! First, `x[[0, 2]] = -1` sets indices 0 and 2 to `-1`, making `x` equal to `[-1, -5, -1, -3]`. Then `x[x < 0] = 0` sets all negative elements to `0`, resulting in `[0, 0, 0, 0]`.",
    {
        "A": "Correct. Left-hand-side (`__setitem__`) fancy indexing and boolean masking mutate `x` in-place: first `x` becomes `[-1, -5, -1, -3]`, and then all negative entries become `0` (`[0, 0, 0, 0]`).",
        "B": "Incorrect. `x[[0, 2]] = -1` mutates `x` in-place via `__setitem__`, so elements 0 and 2 become `-1` and are then zeroed by `x[x < 0] = 0`. (Note: chaining `x[[0, 2]][0] = -1` would fail to mutate `x` because `x[[0, 2]]` calls `__getitem__` first!).",
        "C": "Incorrect. `x[x < 0] = 0` also mutates `x` in-place via `__setitem__`.",
        "D": "Incorrect. Direct single-bracket assignment `x[idx] = val` invokes `__setitem__` and modifies `x` in-place."
    },
    "Understand in-place mutation when advanced or boolean indexing is used in __setitem__ assignment",
    "PyTorch Docs: Tensor Indexing"
)

print(f"Loaded {len(questions)} total questions after A3.")

A4 = "A4: Tensor Operations, Reductions & Linear Algebra"

add_q(
    "PTCA-F-083", A4, "Easy", False,
    "What happens when you attempt to perform an element-wise binary operation (`a + b` or `a * b`) on two tensors `a = torch.rand(2, 3)` and `b = torch.rand(3, 2)` that have the same total number of elements (`6`) but incompatible shapes?",
    "import torch\na = torch.rand(2, 3)\nb = torch.rand(3, 2)\n# Evaluate a * b",
    {
        "A": "It raises a `RuntimeError: The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 1` because element-wise operations require broadcast-compatible shapes, not merely equal element counts.",
        "B": "It automatically performs matrix multiplication (`a @ b`) and returns a `(2, 2)` tensor.",
        "C": "It flattens both tensors to 1D vectors of length 6, multiplies them element-wise, and returns shape `(2, 3)`.",
        "D": "It transposes `b` automatically to `(2, 3)` so the element-wise operation succeeds."
    },
    ["A"],
    "As explicitly demonstrated in Module 2 (`3_tensor_operations.ipynb`), binary operators `+`, `-`, `*`, `/` are strictly element-wise and follow broadcasting rules from trailing dimensions. Because trailing dimensions `3 != 2` and neither is `1`, `a * b` raises a `RuntimeError` even though both tensors contain 6 elements.",
    {
        "A": "Correct. Element-wise operators check broadcasting rules per dimension (`3 != 2`), raising a `RuntimeError`.",
        "B": "Incorrect. `*` is element-wise Hadamard multiplication; matrix multiplication requires `@` or `torch.matmul(a, b)`.",
        "C": "Incorrect. PyTorch never implicitly reshapes or flattens operands for element-wise arithmetic.",
        "D": "Incorrect. PyTorch never implicitly transposes operands to make shapes match."
    },
    "Identify shape compatibility requirements for element-wise arithmetic operations",
    "modules/module_2_tensors/3_tensor_operations.ipynb"
)

add_q(
    "PTCA-F-084", A4, "Medium", False,
    "What is the output of the following code applying `torch.ceil`, `torch.floor`, `torch.round`, and `torch.clamp`?",
    "import torch\n\nx = torch.tensor([-2.5, -0.5, 0.5, 2.5])\nr = torch.round(x)\nc = torch.clamp(torch.ceil(x), min=-1.0, max=2.0)\nf = torch.floor(x)\nprint(r.tolist(), c.tolist(), f.tolist())",
    {
        "A": "[-2.0, -0.0, 0.0, 2.0] [-1.0, -0.0, 1.0, 2.0] [-3.0, -1.0, 0.0, 2.0]",
        "B": "[-3.0, -1.0, 1.0, 3.0] [-1.0, 0.0, 1.0, 2.0] [-2.0, 0.0, 0.0, 2.0]",
        "C": "[-2.0, -0.0, 0.0, 2.0] [-2.0, -0.0, 1.0, 3.0] [-3.0, -1.0, 0.0, 2.0]",
        "D": "[-2.0, -1.0, 1.0, 2.0] [-1.0, 0.0, 1.0, 2.0] [-3.0, -1.0, 0.0, 2.0]"
    },
    ["A"],
    "`torch.round()` uses round-half-to-even (banker's rounding): `-2.5 -> -2.0`, `-0.5 -> -0.0`, `0.5 -> 0.0`, `2.5 -> 2.0`. `torch.ceil(x)` rounds toward $+\infty$ (`[-2.0, -0.0, 1.0, 3.0]`), and clamping to `[-1.0, 2.0]` bounds `-2.0` to `-1.0` and `3.0` to `2.0`, giving `[-1.0, -0.0, 1.0, 2.0]`. `torch.floor(x)` rounds toward $-\infty$, giving `[-3.0, -1.0, 0.0, 2.0]`.",
    {
        "A": "Correct. `round` rounds halfway cases to the nearest even integer (`-2.0, 0.0, 0.0, 2.0`), `ceil` followed by `clamp(-1, 2)` gives `[-1.0, -0.0, 1.0, 2.0]`, and `floor` gives `[-3.0, -1.0, 0.0, 2.0]`.",
        "B": "Incorrect. `round` uses round-to-even (not away-from-zero), and `floor(-2.5)` is `-3.0` (not `-2.0`).",
        "C": "Incorrect. `clamp(min=-1.0, max=2.0)` clips `-2.0` up to `-1.0` and `3.0` down to `2.0`.",
        "D": "Incorrect. `round(-0.5)` and `round(0.5)` both round to the nearest even integer `0.0`."
    },
    "Apply rounding (round, ceil, floor) and range clipping (clamp) operations",
    "modules/module_2_tensors/3_tensor_operations.ipynb"
)

add_q(
    "PTCA-F-085", A4, "Medium", False,
    "In Module 2 (`3_tensor_operations.ipynb`), `torch.asin(torch.sin(x))` is evaluated on `x = torch.tensor([0, math.pi / 4, math.pi / 2, 3 * math.pi / 4])`. What value is returned for the fourth element (`3 * math.pi / 4`), and what happens if `torch.log(torch.tensor([-1.0, 0.0, 1.0]))` is evaluated on real floats?",
    "import math, torch\nx = torch.tensor([0.0, math.pi / 4, math.pi / 2, 3 * math.pi / 4])\ninv = torch.asin(torch.sin(x))\nl = torch.log(torch.tensor([-1.0, 0.0, 1.0]))\nprint(round(inv[3].item(), 4), round(math.pi / 4, 4), torch.isnan(l[0]).item(), l[1].item(), l[2].item())",
    {
        "A": "0.7854 0.7854 True -inf 0.0",
        "B": "2.3562 0.7854 False -inf 0.0",
        "C": "0.7854 0.7854 False 0.0 1.0",
        "D": "It raises a `ValueError: math domain error` on `torch.log(-1.0)`."
    },
    ["A"],
    "The principal range of `torch.asin` is $[-\\pi/2, \\pi/2]$. Because $\\sin(3\\pi/4) = \\sin(\\pi/4) = \\sqrt{2}/2$, `torch.asin(torch.sin(3 * math.pi / 4))` returns $\\pi/4 \\approx 0.7854$ (not $3\\pi/4 \\approx 2.3562$). For real floating-point tensors, `torch.log` does not raise a Python exception on non-positive inputs: `log(-1.0)` yields `nan` (`isnan == True`), `log(0.0)` yields `-inf`, and `log(1.0)` yields `0.0`.",
    {
        "A": "Correct. `asin(sin(3*pi/4))` maps into the principal branch `pi/4` (`0.7854`), and `torch.log([-1., 0., 1.])` produces `[nan, -inf, 0.0]`.",
        "B": "Incorrect. `3 * math.pi / 4` (`2.3562`) lies outside `asin`'s principal range $[-\\pi/2, \\pi/2]$, and `log(-1.0)` is `nan`.",
        "C": "Incorrect. `log(-1.0)` is `nan`, `log(0.0)` is `-inf`, and `log(1.0)` is `0.0`.",
        "D": "Incorrect. Unlike Python's `math.log(-1.0)`, `torch.log` follows IEEE 754 floating-point semantics and returns `nan`/`-inf` without raising an exception."
    },
    "Evaluate inverse trigonometric principal values (sin/asin) and IEEE 754 domain behavior in exp/log",
    "modules/module_2_tensors/3_tensor_operations.ipynb"
)

add_q(
    "PTCA-F-086", A4, "Medium", False,
    "Compare `torch.eq(a, b)`, `torch.equal(a, b)`, and `torch.allclose(a, b)` in the code snippet below. What is printed?",
    "import torch\n\na = torch.tensor([[1.0, 2.0], [3.0, 4.0]])\nb = torch.ones(1, 2)\nc = a + 1e-7\n\nres_eq = torch.eq(a, b)\nres_equal = torch.equal(a, b)\nres_close = torch.allclose(a, c)\nprint(res_eq.shape, res_eq.dtype, res_equal, res_close)",
    {
        "A": "torch.Size([2, 2]) torch.bool False True",
        "B": "torch.Size([1, 2]) torch.bool False False",
        "C": "torch.Size([2, 2]) torch.uint8 True True",
        "D": "It raises a `RuntimeError` in `torch.equal(a, b)` because `a` and `b` have different shapes."
    },
    ["A"],
    "`torch.eq(a, b)` (or `a == b`) performs broadcasted element-wise equality comparison, broadcasting `(2, 2)` and `(1, 2)` to a `torch.bool` tensor of shape `(2, 2)` (as shown in `3_tensor_operations.ipynb`). `torch.equal(a, b)` returns a single Python `bool` (`True` only if `a` and `b` have the exact same shape and identical elements, returning `False` without error when shapes differ). `torch.allclose(a, c)` returns a single Python `bool` (`True`) checking $|a - c| \\le \\text{atol} + \\text{rtol} \\times |c|$ (with default `rtol=1e-05, atol=1e-08`).",
    {
        "A": "Correct. `torch.eq` broadcasts to a `(2, 2)` `bool` tensor, `torch.equal` returns Python `False` for differing shapes/values, and `torch.allclose` returns `True` within tolerance.",
        "B": "Incorrect. Broadcasting `(2, 2)` and `(1, 2)` yields `(2, 2)`, and `1e-7` is well within `allclose` default relative tolerance `1e-5`.",
        "C": "Incorrect. `torch.eq` returns `torch.bool` (not `uint8`), and `torch.equal(a, b)` is `False`.",
        "D": "Incorrect. `torch.equal(a, b)` safely returns `False` when two tensors have different shapes."
    },
    "Distinguish element-wise torch.eq from scalar-returning torch.equal and tolerance-based torch.allclose",
    "modules/module_2_tensors/3_tensor_operations.ipynb"
)

add_q(
    "PTCA-F-087", A4, "Medium", False,
    "What happens when you call `torch.mean(x)` or `torch.std(x)` on an integer tensor `x = torch.tensor([1, 2, 3, 4])` (`dtype=torch.int64`), whereas `torch.sum(x)` and `torch.prod(x)` succeed?",
    "import torch\nx = torch.tensor([1, 2, 3, 4]) # dtype is torch.int64\ns = torch.sum(x)\np = torch.prod(x)\n# What happens on torch.mean(x) or torch.std(x)?",
    {
        "A": "`torch.mean(x)` and `torch.std(x)` raise a `RuntimeError` (`mean(): could not infer output dtype. Input dtype must be either a floating point or complex dtype`), requiring `x.float()` or `torch.mean(x, dtype=torch.float32)`.",
        "B": "`torch.mean(x)` automatically promotes `x` to `torch.float32` and returns `tensor(2.5000)`.",
        "C": "`torch.mean(x)` performs integer floor division and returns `tensor(2, dtype=torch.int64)`.",
        "D": "`torch.sum(x)` also raises a `RuntimeError` on `int64` tensors."
    },
    ["A"],
    "In PyTorch, statistical reductions like `torch.mean`, `torch.std`, and `torch.var` do NOT automatically cast integer tensors to floats; calling `torch.mean(torch.tensor([1, 2, 3, 4]))` raises `RuntimeError: mean(): could not infer output dtype. Input dtype must be either a floating point or complex dtype`. You must either create a float tensor (`torch.tensor([1., 2., 3., 4.])` as in `3_tensor_operations.ipynb`), cast `x.float()`, or pass `dtype=torch.float32` to `torch.mean`.",
    {
        "A": "Correct. `mean`, `std`, and `var` require floating-point or complex inputs (or an explicit `dtype=` keyword argument for `mean`).",
        "B": "Incorrect. Unlike NumPy (which auto-promotes `np.mean` on ints to `float64`), PyTorch raises a `RuntimeError`.",
        "C": "Incorrect. `torch.mean` never truncates to an integer.",
        "D": "Incorrect. `torch.sum(x)` and `torch.prod(x)` work on integer tensors and return a `torch.int64` scalar tensor."
    },
    "Handle floating-point dtype requirements in statistical reductions (mean, std, var)",
    "modules/module_2_tensors/3_tensor_operations.ipynb"
)

add_q(
    "PTCA-F-088", A4, "Hard", False,
    "By default, how does PyTorch's `torch.var(x)` / `torch.std(x)` differ from NumPy's `np.var(x)` / `np.std(x)` regarding Bessel's correction (`correction` / `unbiased`)?",
    "import torch\nx = torch.tensor([1.0, 2.0, 3.0])\nprint(torch.var(x).item(), torch.var(x, correction=0).item())",
    {
        "A": "1.0 0.6666666865348816",
        "B": "0.6666666865348816 1.0",
        "C": "1.0 1.0",
        "D": "2.0 0.6666666865348816"
    },
    ["A"],
    "By default, PyTorch's `torch.var(x)` and `torch.std(x)` apply Bessel's correction (`correction=1`, formerly `unbiased=True`), dividing the sum of squared deviations by $N - 1$: for `[1.0, 2.0, 3.0]`, $((1-2)^2 + (2-2)^2 + (3-2)^2) / (3 - 1) = 2 / 2 = 1.0$. Passing `correction=0` (or `unbiased=False`, matching NumPy's default `ddof=0`) divides by $N = 3$, yielding $2 / 3 \\approx 0.6667$.",
    {
        "A": "Correct. Default `correction=1` divides by $N - 1 = 2$ giving `1.0`, while `correction=0` divides by $N = 3$ giving `2/3`.",
        "B": "Incorrect. This reverses PyTorch's default (`correction=1`) and `correction=0`.",
        "C": "Incorrect. `correction=0` disables Bessel's correction and divides by $N$.",
        "D": "Incorrect. `2.0` is the unnormalized sum of squared deviations before dividing by $N - 1$ or $N$."
    },
    "Understand Bessel's correction default (correction=1 / unbiased=True) in torch.var and torch.std",
    "modules/module_2_tensors/3_tensor_operations.ipynb & PyTorch Docs: torch.var"
)

add_q(
    "PTCA-F-089", A4, "Medium", False,
    "Given a 2D matrix `x = torch.ones(4, 5)` (4 rows, 5 columns), what are the shapes of `x.sum(dim=0)`, `x.sum(dim=1)`, and `x.sum(dim=1, keepdim=True)`, and why is `keepdim=True` needed if you want to normalize each row via `x / row_sums`?",
    "import torch\nx = torch.ones(4, 5)\ns0 = x.sum(dim=0)\ns1 = x.sum(dim=1)\ns1_keep = x.sum(dim=1, keepdim=True)\nprint(s0.shape, s1.shape, s1_keep.shape)",
    {
        "A": "`torch.Size([5])`, `torch.Size([4])`, `torch.Size([4, 1])`; without `keepdim=True`, dividing `(4, 5)` by `(4,)` fails to broadcast because trailing dimensions `5` and `4` do not match, whereas `(4, 5)` and `(4, 1)` broadcast cleanly across columns.",
        "B": "`torch.Size([4])`, `torch.Size([5])`, `torch.Size([1, 5])`; `dim=0` sums across columns and `dim=1` sums across rows.",
        "C": "`torch.Size([1, 5])`, `torch.Size([4, 1])`, `torch.Size([4, 5])`; `keepdim=True` expands the result back to the original shape `(4, 5)`.",
        "D": "`torch.Size([5])`, `torch.Size([4])`, `torch.Size([4, 1])`; dividing `(4, 5)` by `(4,)` works without `keepdim=True` because PyTorch aligns leading dimensions."
    },
    ["A"],
    "Reducing along `dim=0` collapses the 4 rows into `torch.Size([5])` (one sum per column). Reducing along `dim=1` collapses the 5 columns into `torch.Size([4])` (one sum per row). If you attempt `x / s1` with shapes `(4, 5)` and `(4,)`, broadcasting aligns trailing dimensions (`5` vs `4`) and raises a `RuntimeError`. Using `keepdim=True` retains the reduced dimension with length `1` (`(4, 1)`), so `(4, 5) / (4, 1)` broadcasts properly.",
    {
        "A": "Correct. `dim=0` collapses axis 0 (`(5,)`), `dim=1` collapses axis 1 (`(4,)`), and `keepdim=True` keeps `(4, 1)` so trailing-dimension broadcasting succeeds.",
        "B": "Incorrect. `dim=0` reduces axis 0 (size 4), leaving axis 1 (size 5).",
        "C": "Incorrect. `keepdim=False` is the default, and `keepdim=True` keeps size `1` (`(4, 1)`), not `5`.",
        "D": "Incorrect. Broadcasting in PyTorch always aligns **trailing** (rightmost) dimensions, so `(4, 5)` and `(4,)` are not broadcastable."
    },
    "Use dim and keepdim=True in reductions to preserve broadcast compatibility",
    "modules/module_2_tensors/4_tensor_broadcasting.ipynb"
)

add_q(
    "PTCA-F-090", A4, "Medium", False,
    "How does `torch.max(x)` (with no `dim` argument) differ in return type from `torch.max(x, dim=1)` on a 2D tensor `x`?",
    "import torch\n\nx = torch.tensor([[10, 50, 30],\n                  [40, 20, 60]])\nm_all = torch.max(x)\nm_dim = torch.max(x, dim=1)\nprint(type(m_all), m_all.item(), len(m_dim), m_dim.values.tolist(), m_dim.indices.tolist())",
    {
        "A": "<class 'torch.Tensor'> 60 2 [50, 60] [1, 2]",
        "B": "<class 'torch.Tensor'> 60 2 [40, 50, 60] [1, 0, 1]",
        "C": "<class 'tuple'> 60 2 [50, 60] [10, 20]",
        "D": "<class 'torch.Tensor'> 60 1 [60] [5]"
    },
    ["A"],
    "When called without a `dim` argument, `torch.max(x)` (and `torch.min(x)`) returns a single 0D `torch.Tensor` containing the global maximum value (`60`). When called with a `dim` argument (`torch.max(x, dim=1)`), it returns a 2-element named tuple `(values, indices)` where `.values` contains the maximum of each row (`[50, 60]`) and `.indices` contains the `argmax` column indices (`[1, 2]`). (To get only values along a dimension without indices, `torch.amax(x, dim=1)` can also be used).",
    {
        "A": "Correct. `torch.max(x)` returns a single scalar tensor (`60`), while `torch.max(x, dim=1)` returns a named tuple `(values=tensor([50, 60]), indices=tensor([1, 2]))`.",
        "B": "Incorrect. `[40, 50, 60]` and `[1, 0, 1]` correspond to `dim=0` (column-wise max), not `dim=1` (row-wise max).",
        "C": "Incorrect. `m_all` is a `torch.Tensor` (not a tuple), and `m_dim.indices` holds integer indices `[1, 2]`, not minimum values.",
        "D": "Incorrect. `torch.max(x, dim=1)` returns a 2-tuple `(values, indices)`."
    },
    "Distinguish global torch.max(x) tensor return from dimensional torch.max(x, dim) (values, indices) return",
    "modules/module_2_tensors/3_tensor_operations.ipynb"
)

add_q(
    "PTCA-F-091", A4, "Medium", False,
    "What does `torch.argmax(x)` return when called WITHOUT a `dim` argument on a 2D tensor `x`?",
    "import torch\n\nx = torch.tensor([[10, 50, 30],\n                  [40, 20, 60]])\nidx_flat = torch.argmax(x)\nidx_col = torch.argmax(x, dim=1)\nprint(idx_flat.item(), idx_col.tolist())",
    {
        "A": "5 [1, 2]",
        "B": "[1, 2] [1, 2]",
        "C": "2 [1, 2]",
        "D": "60 [50, 60]"
    },
    ["A"],
    "`torch.argmax(x)` (and `torch.argmin(x)`) returns the index of the maximum value. When `dim=None` (the default), it returns the scalar index into the **flattened** tensor: `60` is at row 1, col 2, which is flat index $1 \\times 3 + 2 = 5$. When `dim=1` is specified, it returns the index of the maximum along dimension 1 for each row: `[1, 2]`.",
    {
        "A": "Correct. Without `dim`, `argmax` returns the flattened index `5` (for `60`); with `dim=1`, it returns `[1, 2]`.",
        "B": "Incorrect. `torch.argmax(x)` without `dim` returns a single 0D index into the flattened tensor, not a 2D coordinate tuple.",
        "C": "Incorrect. `2` is the column index of `60`, but flattened index across the `(2, 3)` tensor is `5`.",
        "D": "Incorrect. `60` and `[50, 60]` are the maximum values (`max`), whereas `argmax` returns the `int64` indices."
    },
    "Find flat and dimensional indices of extrema using torch.argmax and torch.argmin",
    "PyTorch Docs: torch.argmax and torch.argmin"
)

add_q(
    "PTCA-F-092", A4, "Medium", False,
    "What is the output of the following code using `torch.unique` with `return_counts=True`?",
    "import torch\n\nx = torch.tensor([3, 1, 2, 1, 2, 1])\nvals, counts = torch.unique(x, sorted=True, return_counts=True)\nprint(vals.tolist(), counts.tolist())",
    {
        "A": "[1, 2, 3] [3, 2, 1]",
        "B": "[3, 1, 2] [1, 3, 2]",
        "C": "[1, 2, 3] [1, 2, 3]",
        "D": "[1, 1, 1, 2, 2, 3] [3, 2, 1]"
    },
    ["A"],
    "`torch.unique(x, sorted=True, return_counts=True)` deduplicates the tensor into sorted unique values `[1, 2, 3]` and returns a second tensor `counts` containing the frequency of each unique value in `x` (`1` appears 3 times, `2` appears 2 times, `3` appears 1 time -> `[3, 2, 1]`).",
    {
        "A": "Correct. Sorted unique values are `[1, 2, 3]` and their occurrence counts are `[3, 2, 1]`.",
        "B": "Incorrect. `sorted=True` orders the unique elements ascending as `[1, 2, 3]`.",
        "C": "Incorrect. `1` occurs 3 times and `3` occurs 1 time.",
        "D": "Incorrect. `vals` contains only the unique deduplicated elements `[1, 2, 3]`."
    },
    "Extract unique elements and occurrence frequencies with torch.unique",
    "modules/module_2_tensors/3_tensor_operations.ipynb"
)

add_q(
    "PTCA-F-093", A4, "Medium", False,
    "Compare `torch.topk(x, k=2)` and `torch.sort(x, descending=True)` on a 1D tensor `x = torch.tensor([10.0, 50.0, 20.0, 40.0])`. What is printed?",
    "import torch\n\nx = torch.tensor([10.0, 50.0, 20.0, 40.0])\ntop_vals, top_idx = torch.topk(x, k=2)\nsort_vals, sort_idx = torch.sort(x, descending=True)\nprint(top_vals.tolist(), top_idx.tolist(), len(sort_vals))",
    {
        "A": "[50.0, 40.0] [1, 3] 4",
        "B": "[10.0, 20.0] [0, 2] 4",
        "C": "[50.0, 40.0] [50, 40] 2",
        "D": "[40.0, 50.0] [3, 1] 4"
    },
    ["A"],
    "Both `torch.topk` and `torch.sort` return a `(values, indices)` named tuple. By default, `torch.topk(x, k=2)` has `largest=True` and `sorted=True`, returning the `2` largest values `[50.0, 40.0]` and their original indices `[1, 3]`. `torch.sort(x, descending=True)` sorts all `4` elements in descending order.",
    {
        "A": "Correct. `topk(x, k=2)` returns the top 2 values `[50.0, 40.0]` and their indices `[1, 3]`, while `sort` returns all 4 sorted elements.",
        "B": "Incorrect. `torch.topk` defaults to `largest=True`; to get the smallest `k` elements, you must pass `largest=False`.",
        "C": "Incorrect. `top_idx` contains original indices `[1, 3]`, and `sort_vals` has length `4`.",
        "D": "Incorrect. With `sorted=True` (default), `topk` orders the largest elements from highest (`50.0` at index `1`) to lowest (`40.0` at index `3`)."
    },
    "Retrieve top-k predictions and sorted orderings using torch.topk and torch.sort",
    "PyTorch Docs: torch.topk and torch.sort"
)

add_q(
    "PTCA-F-094", A4, "Hard", False,
    "Which option accurately states the input rank constraints of `torch.dot`, `torch.mv`, `torch.mm`, and `torch.bmm`?",
    "import torch\n# Compare strict linear algebra functions vs general @ / torch.matmul",
    {
        "A": "`torch.dot` requires two 1D vectors; `torch.mv` requires a 2D matrix and a 1D vector; `torch.mm` requires two 2D matrices (no broadcasting); and `torch.bmm` requires two 3D tensors `(B, N, M)` and `(B, M, P)` with matching batch size `B`.",
        "B": "`torch.dot` supports 1D, 2D, and 3D tensors just like `np.dot` in NumPy.",
        "C": "`torch.mm` automatically broadcasts batch dimensions on 3D and 4D tensors just like `torch.matmul` (`@`).",
        "D": "`torch.bmm` broadcasts `(1, N, M)` against `(B, M, P)` automatically."
    },
    ["A"],
    "Unlike `np.dot` in NumPy, PyTorch's specialized linear algebra ops enforce strict dimensionality checks without broadcasting: `torch.dot(1D, 1D) -> 0D scalar`, `torch.mv(2D, 1D) -> 1D vector`, `torch.mm(2D, 2D) -> 2D matrix`, and `torch.bmm((B, N, M), (B, M, P)) -> (B, N, P)` (where both inputs must be 3D with identical batch size `B`). General polymorphic dispatch and batch broadcasting are handled by `torch.matmul` (the `@` operator).",
    {
        "A": "Correct. Each specialized function (`dot`, `mv`, `mm`, `bmm`) enforces strict input ranks and does not broadcast batch dimensions.",
        "B": "Incorrect. Unlike `np.dot`, `torch.dot` strictly requires both inputs to be 1D vectors (`RuntimeError: 1D tensors expected`).",
        "C": "Incorrect. `torch.mm` raises a `RuntimeError` if either input is not 2D.",
        "D": "Incorrect. `torch.bmm` does NOT broadcast the batch dimension `B`; if batch sizes differ (`1` vs `B`), `torch.bmm` raises a `RuntimeError` whereas `torch.matmul` (`@`) broadcasts them."
    },
    "Differentiate strict rank constraints of dot, mv, mm, and bmm from polymorphic matmul (@)",
    "PyTorch Docs: torch.dot, torch.mv, torch.mm, torch.bmm, and torch.matmul"
)

add_q(
    "PTCA-F-095", A4, "Hard", False,
    "In transformer multi-head attention, queries `Q` have shape `(32, 8, 128, 64)` (`batch=32, heads=8, seq_len=128, head_dim=64`) and transposed keys `K_T` have shape `(1, 8, 64, 128)`. What is the output shape of `scores = Q @ K_T` (`torch.matmul(Q, K_T)`), and why would `torch.bmm(Q, K_T)` fail here?",
    "import torch\n\nQ = torch.empty(32, 8, 128, 64)\nK_T = torch.empty(1, 8, 64, 128)\nscores = Q @ K_T\nprint(scores.shape)",
    {
        "A": "`scores.shape` is `torch.Size([32, 8, 128, 128])` because `@` (`torch.matmul`) performs matrix multiplication on the last two dimensions `(128, 64) x (64, 128) -> (128, 128)` while broadcasting the leading batch dimensions `(32, 8)` and `(1, 8) -> (32, 8)`; `torch.bmm` would fail because `bmm` only accepts 3D tensors and does not broadcast batch dimensions.",
        "B": "`scores.shape` is `torch.Size([32, 8, 64, 64])` because `@` contracts the dimension of size 128.",
        "C": "`Q @ K_T` raises a `RuntimeError` because batch dimension 0 (`32` vs `1`) must be identical in `torch.matmul`.",
        "D": "`scores.shape` is `torch.Size([32, 8, 128, 128])`, and `torch.bmm(Q, K_T)` produces the exact same 4D result."
    },
    ["A"],
    "For inputs with `ndim > 2`, `torch.matmul` (`@`) treats the last two axes as matrices (`(128, 64)` multiplied by `(64, 128)` -> `(128, 128)`) and treats all preceding axes (`(32, 8)` and `(1, 8)`) as batch dimensions subject to standard broadcasting rules (`(32, 8)`), producing `torch.Size([32, 8, 128, 128])`. `torch.bmm` strictly requires 3D inputs `(B, N, M)` and `(B, M, P)` with equal `B`.",
    {
        "A": "Correct. `@` contracts the inner dimension `64` over the last two axes (`(128, 128)`) and broadcasts batch axes `(32, 8)` and `(1, 8)` to `(32, 8)`, while `bmm` rejects 4D inputs and unbroadcasted batch sizes.",
        "B": "Incorrect. Multiplying `(128, 64)` by `(64, 128)` contracts the inner dimension `64`, producing `(128, 128)`.",
        "C": "Incorrect. `torch.matmul` (`@`) supports full broadcasting across all leading dimensions before the last two axes.",
        "D": "Incorrect. `torch.bmm` raises `RuntimeError: batch1 must be a 3D tensor` on 4D inputs."
    },
    "Compute batched matrix multiplications with broadcasting using @ / torch.matmul",
    "modules/module_2_tensors/4_tensor_broadcasting.ipynb & PyTorch Docs: torch.matmul"
)

import random

rng = random.Random(42)
letters = ["A", "B", "C", "D"]
for idx, q in enumerate(questions):
    if not q["multi_select"]:
        target_letter = letters[idx % 4]
        cur_letter = q["correct"][0]
        if cur_letter != target_letter:
            q["options"][cur_letter], q["options"][target_letter] = (
                q["options"][target_letter],
                q["options"][cur_letter],
            )
            q["option_explanations"][cur_letter], q["option_explanations"][target_letter] = (
                q["option_explanations"][target_letter],
                q["option_explanations"][cur_letter],
            )
            q["correct"] = [target_letter]
    else:
        perm = letters[:]
        rng.shuffle(perm)
        old_opts = q["options"].copy()
        old_exps = q["option_explanations"].copy()
        old_correct = set(q["correct"])
        new_opts = {}
        new_exps = {}
        new_correct = []
        for new_L, old_L in zip(letters, perm):
            new_opts[new_L] = old_opts[old_L]
            new_exps[new_L] = old_exps[old_L]
            if old_L in old_correct:
                new_correct.append(new_L)
        q["options"] = new_opts
        q["option_explanations"] = new_exps
        q["correct"] = sorted(new_correct)

out_path = os.path.join(os.path.dirname(__file__), "domain_a1.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Successfully wrote {len(questions)} questions to {out_path}")

