class StackError(Exception):
    """Base class for stack-related exceptions."""
    pass


class StackEmptyError(StackError):
    """Raised when attempting to pop from an empty stack."""
    pass


class StackFullError(StackError):
    """Raised when attempting to push to a full stack."""
    pass


class SimpleStack:
    """Base class for a simple stack implementation."""
    __slots__ = ['_stack']

    def __init__(self):
        self._stack = []

    def push(self, item):
        """Add an item to the stack."""
        self._stack.append(item)

    def pop(self):
        """Remove and return the top item of the stack."""
        if not self._stack:
            raise StackEmptyError("Cannot pop from an empty stack.")
        return self._stack.pop()

    def __repr__(self):
        """String representation of the stack."""
        return f"SimpleStack({self._stack})"

    def __len__(self):
        """Return the size of the stack."""
        return len(self._stack)

    def __iter__(self):
        """Make the stack iterable."""
        return iter(self._stack)

    @classmethod
    def from_list(cls, lst, **kwargs):
        """
        Create a stack from a list.

        Parameters:
            - lst: List of elements to initialize the stack.
            - kwargs: Additional arguments like max_size and data_type.

        Returns:
            - An instance of the calling class initialized with the given list.
        """
        # Instantiate the class dynamically
        stack = cls(**kwargs)
        # Push each item, leveraging the push method to enforce constraints
        for item in lst:
            stack.push(item)
        return stack


class MaxSizeStack(SimpleStack):
    """Stack with a maximum size restriction."""

    def __init__(self, **kwArgs):
        if "max_size" not in kwArgs:
            raise AttributeError(f"Parameter 'max_size' missing from the arguments passed - {[key for key in kwArgs]}")
        
        self.max_size = kwArgs.pop("max_size")
        super().__init__(**kwArgs)
        
    def push(self, item):
        """Add an item to the stack, enforcing max size."""
        if len(self) >= self.max_size:
            raise StackFullError("Stack is full, cannot push more items.")
        super().push(item)


class TypedStack(SimpleStack):
    """Stack that only accepts elements of a specific type."""

    def __init__(self, **kwArgs):
        if "data_type" not in kwArgs:
            raise AttributeError(f"Parameter 'data_type' missing from the arguments passed - {[key for key in kwArgs]}")
        
        self.data_type = kwArgs.pop("data_type")
        super().__init__(**kwArgs)

    def push(self, item):
        """Add an item to the stack, enforcing type restrictions."""
        self._validate_item(item, self.data_type)
        super().push(item)

    @staticmethod
    def _validate_item(item, data_type):
        """Validate that the item is of the correct type."""
        # print(">>", type(data_type), data_type)
        if not isinstance(item, data_type):
            raise TypeError(f"Invalid item type: {type(item)}. Must be [{data_type}]")


class MaxTypedStack(MaxSizeStack, TypedStack):
    """Stack that enforces both maximum size and type restrictions."""

    def __init__(self, **kwargs):
        # max_size = kwargs.pop('max_size', None)
        # data_type = kwargs.pop('data_type', None)

        # # Initialize both parent classes with appropriate arguments
        # MaxSizeStack.__init__(self, max_size=max_size)
        # TypedStack.__init__(self, data_type=data_type)

        super().__init__(**kwargs)

    def push(self, item):
        """Add an item, enforcing both max size and type restrictions."""
        # TypedStack._validate_item(item)  # Validate the item's type
        # MaxSizeStack.push(self, item)   # Enforce max size using MaxSizeStack logic
        super().push(item)

    def __add__(self, other):
        """Combine two stacks into one."""
        if not isinstance(other, SimpleStack):
            raise TypeError("Can only combine with another stack.")
        combined_stack = MaxTypedStack(max_size=self.max_size + other.max_size, data_type=self.data_type)
        combined_stack._stack = self._stack + other._stack
        return combined_stack

# Testing the Implementation
def main():
    # Create a MaxTypedStack with max size 5 and type int
    stack = MaxTypedStack(max_size=5, data_type=int)

    print("Pushing items to stack:")
    stack.push(10)
    stack.push(20)
    print(stack)

    print("\nAttempting to push invalid type:")
    try:
        stack.push(15.5)  # Invalid type
    except TypeError as e:
        print(f"EXCEPTION: {e}")

    print("\nAttempting to push beyond max size:")
    try:
        stack.push(30)
        stack.push(40)
        stack.push(50)
        stack.push(60)  # Exceeds max size
    except StackFullError as e:
        print(f"EXCEPTION: {e}")

    print("\nPopping items from the stack:")
    while len(stack) > 0:
        print(f"Popped: {stack.pop()}")

    print("\nAttempting to pop from an empty stack:")
    try:
        stack.pop()  # Empty stack
    except StackEmptyError as e:
        print(f"EXCEPTION: {e}")

    print("\nDemonstrating operator overloading:")
    stack1 = MaxTypedStack(max_size=3, data_type=int)
    stack2 = MaxTypedStack(max_size=3, data_type=int)
    stack1.push(1)
    stack1.push(2)
    stack2.push(3)
    stack2.push(4)

    combined_stack = stack1 + stack2
    print(f"Combined Stack: {combined_stack}")

    print("\nUsing iterators:")
    for item in combined_stack:
        print(item)

    print("\nCreating a stack from a list:")
    stack_from_list = MaxTypedStack.from_list([10, 20, 30], data_type=int, max_size=10)
    ## Exercise: Investigation
    # Does this really create the specified type stack, or always defaults to SimpleStack?
    # Identify the cause.
    # Find the remedy


    print(stack_from_list)


if __name__ == "__main__":
    main()
