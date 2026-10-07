from typing import Dict, Any, Iterator, Optional
from collections import abc
from types import FunctionType
import inspect


_UNBOUND = object() #marker for a local variable that exists syntactically but has not recieved a value yet


class DynamicScope(abc.Mapping): #this is a mapping that contains the variables visible through the dynamic scope
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {} 
        
    def __getitem__(self, key):
        if key not in self.env:
            raise NameError(f"{key!r} does not exist in the dynamic reference environment")
    
            
    
        value = self.env[key]        
        if value is _UNBOUND:
         raise UnboundLocalError(
              f"local variable {key!r} referenced before assignment"
          )

        return value
        

    def __iter__(self):
        return iter(self.env)

    def __len__(self):
        return len(self.env)    


def get_dynamic_re() -> DynamicScope: #builds the dynamic reference environment from active stack frames
    




# When inspecting an inner function, I ignore co_freevars because
# those variables were not defined by that function.



     
    dynamic_scope = DynamicScope()  #takes a dynamic scope object that we defined which is a .env
    stack_info = inspect.stack() #we inspect all the stack frames 
    
    for i in range(1, len(stack_info)): #ignores the first stack frame which contains information about get_dynamic_re()
        frame = stack_info[i].frame
        
        local_names = (frame.f_code.co_varnames + frame.f_code.co_cellvars) 
        # frame.f_locals can contain both true locals and free variables captured. we do not want the free variables
        # frame.f_code.co_varnames gives the function's true local variables
        # Some variables defined by an outer function become cell variables when
        # nested functions reference them and they are the cell variables so I also need frame.f_code.co_cellvars.
        local_vars = {}

       #a stack frame is taken, a local var is built, then checked and added to the final scope environment
       #after that we move to the next stack frame
        for name in local_names: #fill local_vars with true locals and cell variables
        
         if name in dynamic_scope.env:
                continue
            
         if name in frame.f_locals:
            local_vars[name] = frame.f_locals[name]
         else:
             dynamic_scope.env[name] = _UNBOUND #variable is local in syntax but currently unbound
            
        
        for name in local_vars: #if a close frame already gave us this variable then we will ignore it
            if name in dynamic_scope.env:
                pass
            else:
                dynamic_scope.env[name] = local_vars[name]
         
    
    
    
    
    return dynamic_scope
