def main():
    def inner_function(*args, **kwargs):
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)
        
        def nested_function():
            print("This is a nested function")
        
        nested_function()
    
    inner_function(1, 2, 3, a=4, b=5)

if __name__ == "__main__":
    main()