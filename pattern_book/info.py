from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__, static_url_path="/static", static_folder="template")

@app.route('/')
def index():
	return render_template('home.html', yesHome = 'active')

# BUILDER

@app.route('/builder')
def builder():
	name = 'Builder Pattern.'

	forces = '''There is a class that needs to build an object in
		a complex way requiring lots of different parameters
		in the constructor. This causes diffcult code to manage
		and the ability to mix up parameters causing runtime errors.'''

	solution = '''Create a complex objects using simple objects. Take
		all the methods from the objects code and put them
		in their own separate objects. This will make ease to
		step by step 'build' the complex object.'''

	related = ['Singleton pattern.', 'Template Method Pattern.']

	link = '/builderexample'

	return render_template('template.html', yesBuilder = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/builderexample')
def builderExample():
	name = 'Builder Pattern Example.'
	link = 'examples/builderex.html'
	button = '/builder'
	return render_template('tempex.html', yesBuilderex = 'active', name = name, button = button, link = link)

# OBSERVER

@app.route('/observer')
def observer():
	name = 'Observer Pattern.'

	forces = '''When you are building a layered architecture the lower
		layers should have no knowledge of the high layers,
		but the higher layers need to have knowledge of the lower layers.
		There still needs to be communication from the lower layers to the
		high layers by notifying them when things change in the lower layers.'''

	solution = '''The higher layers should addDependents(). This will show that they
		depend on the lower layers and when things change in the lower
		a message will be sent to itself then the higher layers will be
		automatically notified that things have changed.'''

	related = ['Singleton Pattern.', 'Mediator Pattern.', 'Visitor Pattern.']

	link = '/observerexample'

	return render_template('template.html', yesObserver = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/observerexample')
def observerExample():
	name = 'Observer Pattern Example.'
	link = 'examples/observerex.html'
	button = '/observer'
	return render_template('tempex.html', yesObserverex = 'active', name = name, button = button, link = link)

# TEMPLATE METHOD

@app.route('/templatemethod')
def templateMethod():
	name = 'Template Method Pattern.'

	forces = '''Components have many processes that occur multiple times. This
		causes the duplication of code. The steps that are required to
		do such processes are basically the same but the little details
		are different in the slightest way.'''

	solution = '''Make a class, could be abstract, that implements the basics
		of the processes that are similar in the components. Each method
		then can be overridden to be implemented by the individual compontents to the
		specific needs of the details that are different from other
		components using the same template.'''

	related = ['Strategy Pattern.', 'Builder Pattern.', 'State Pattern']

	link = '/templatemethodexample'

	return render_template('template.html', yesTemplate = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/templatemethodexample')
def templateMethodExample():
	name = 'Template Method Pattern Example.'
	link = 'examples/templatemethodex.html'
	button = '/templatemethod'
	return render_template('tempex.html', yesTemplateex = 'active', name = name, button = button, link = link)

# DOUBLE DISPATCH

@app.route('/doubledispatch')
def doubleDispatch():
	name = 'Double Dispatch Pattern.'

	forces = '''This pattern is technically a code smell which will eliminated conditionals.
		A class may have a method with may conditionals to attempt to do something
		different depending on the arguments passed in. '''

	solution = '''Inside the class make seperate methods for each section of the conditional
		with the same name. This will cause the arguments passed into the method to
		descide what method is chosen instead of slow conditionals.'''
	related = ['Template Method Pattern.', 'Singleton Pattern.']

	link = '/doubledispatchexample'

	return render_template('template.html', yesDouble = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/doubledispatchexample')
def doubleDispatchExample():
	name = 'Double Dispatch Pattern Example.'
	link = 'examples/doubledispatchex.html'
	button = '/doubledispatch'
	return render_template('tempex.html', yesDoubleex = 'active', name = name, button = button, link = link)

# NULL OBJECT

@app.route('/nullobject')
def nullObject():
	name = 'Null Object Pattern.'

	forces = '''A class needs to handle edge case when a value is not
		present. Null may be a viable option but many of the methods
		may act differently when a value is not present.'''

	solution = '''You need to create a sub class of the value and name it
                Null and then the class name. Inside the new null class the
                methods should be redefined so they behave the way they
                should if no value is present.'''

	related = ['Singleton Pattern.']

	link = '/nullobjectexample'

	return render_template('template.html', yesNull = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/nullobjectexample')
def nullObjectExample():
	name = 'Null Object Pattern Example.'
	link = 'examples/nullobjectex.html'
	button = '/nullobject'
	return render_template('tempex.html', yesNullex = 'active', name = name, button = button, link = link)

# SINGLETON

@app.route('/singleton')
def singleton():
        name = 'Singleton Pattern.'

        forces = '''You need to access a value globally and there can only be one
		one instance of it in the system.'''

        solution = '''Create a class with the instance variable is an instance of
		the class. Have an accessing method return that instance variable.
		The constructor should be private and have nothing in it forcing
		the use of the accessing method.'''

        related = ['Abstract Factory Pattern.', 'Prototype Pattern.', 'Facade Pattern.', 'State Pattern.']

        link = '/singletonexample'

        return render_template('template.html', yesSingle = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/singletonexample')
def singletonExample():
        name = 'Singleton Pattern Example.'
        link = 'examples/singletonex.html'
        button = '/singleton'
        return render_template('tempex.html', yesSingleex = 'active', name = name, button = button, link = link)

# COMPOSITE

@app.route('/composite')
def composite():
        name = 'Composite Pattern.'

        forces = '''Multiple objects are used in the same way. Individual objects
		are handled differently than the composition of objects. A bunch
		of objects need to behave as if they are just one. This will
		allow all objects, individual and composite, to be treated the
		same.'''

        solution = '''Make an interface for individual and compositions of objects.
		The individual objects will directly implement the compostion and
		will send messages to the individual components.'''

        related = ['Observer Pattern.', 'Template Method Pattern.']

        link = '/compositeexample'

        return render_template('template.html', yesComp = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/compositeexample')
def compositeExample():
        name = 'Composite Pattern Example.'
        link = 'examples/compositeex.html'
        button = '/composite'
        return render_template('tempex.html', yesCompex = 'active', name = name, button = button, link = link)

#DECORATOR

@app.route('/decorator')
def decorator():
	name = 'Decorator Pattern.'

	forces = '''There are objects in whch you want to add something to. You do not
		want to add it to every instance of the object because this would
		create slow and duplicated code.'''

	solution = '''To do this you will need to attach the additional 'something'
		you want to add to the object. To attach it you will need to make
		an abstract decorator that implements the main interface of the
		object. Doing so will not change the behavior of the object but will
		add behavior.'''

	related = ['Singleton Pattern.', 'Wrapper Pattern.']

	link = '/decoratorexample'

	return render_template('template.html', yesDec = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/decoratorexample')
def decoratorExample():
	name = 'Decorator Pattern Example.'
	link = 'examples/decoratorex.html'
	button = '/decorator'
	return render_template('tempex.html', yesDecex = 'active', name = name, button = button, link = link)

#FACADE

@app.route('/facade')
def facade():
        name = 'Facade Pattern.'

        forces = '''There are implementations, of certain objects a class relies on,
		that we want to hide form the client or other objects. For example,
		this may be for polymorphism.'''

        solution = '''We will make a facade class that is the main front of the program.
		The client or other objects using the facade class will talk directly
		to the facade class and the facade class will talk to the hiden classes.'''

        related = ['Strategy Pattern.']

        link = '/facadeexample'

        return render_template('template.html', yesFacade = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/facadeexample')
def facadeExample():
        name = 'Facade Pattern Example.'
        link = 'examples/facadeex.html'
        button = '/facade'
        return render_template('tempex.html', yesFacadeex = 'active', name = name, button = button, link = link)

#VISITOR

@app.route('/visitor')
def visitor():
        name = 'Visitor Pattern.'

        forces = '''You want to add a new behavior to a class without changing anything
		in the existing class code.'''

        solution = '''Add a function that accepts the visitor class to each element of
		the structure. This will allow the visitor to 'visit' them and preform
		the new behavior added to the object. No code will be modified but
		functionality will be added to the object.'''

        related = ['Observer Pattern.', 'Double Dispatch Pattern.', 'Facade Pattern.']

        link = '/visitorexample'

        return render_template('template.html', yesVisit = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/visitorexample')
def visitorExample():
        name = 'Visitor Pattern Example.'
        link = 'examples/visitorex.html'
        button = '/visitor'
        return render_template('tempex.html', yesVisitex = 'active', name = name, button = button, link = link)

#COMMAND

@app.route('/command')
def command():
	name = 'Command Pattern.'

	forces = '''You need to turn a request into an object and have the same behavior as a
		regular object. This means it can be stored in a variable of passed in as an
		object.'''

	solution = '''To do this you will create a class that will act as a service provider
		that can implatment the needed behavior. This service provider class will
		then have a method causes it to do the behavior.'''

	related = ['Composite Pattern.']

	link = '/commandexample'

	return render_template('template.html', yesComm = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/commandexample')
def commandExample():
	name = 'Command Pattern Example.'
	link = 'examples/commandex.html'
	button = '/command'
	return render_template('tempex.html', yesCommex = 'active', name = name, button = button, link = link)

#CHAIN OF RESPONSIBILITY

@app.route('/chain')
def chain():
	name = 'Chain of Responsibility Pattern.'

	forces = '''You want to send a request. The sender of the request cannot be grouped
		with the reciever. This may be because you want more then one object to be
		able to handle the request.'''

	solution = '''You need to have all the recievers to be arranged in a link list.
		When the first reciever object gets the message it may pass it on or
		handle the request. If it chooses to pass the request will continue down
		the list until it is handled by a reciever or given a default value at
		the end.'''

	related = ['Command Pattern.']

	link = '/chainexample'

	return render_template('template.html', yesChain = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/chainexample')
def chainExample():
	name = 'Chain of Responsibility Pattern Example.'
	link = 'examples/chainex.html'
	button = '/chain'
	return render_template('tempex.html', yesChainex = 'active', name = name, button = button, link = link)

#STATE

@app.route('/state')
def state():
        name = 'State Pattern.'

        forces = '''You need an object to change it's behavior at runtime depending on it's state.'''

        solution = '''Instead of having a single state class with many different conditionals,
		spearate the code into their own classes. The use these classes to produce a
		hierarchy of state objects that have the different implementations of the
		interface method.'''

        related = ['Double Dispatch Pattern.', 'Template Method Pattern.']

        link = '/stateexample'

        return render_template('template.html', yesState = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/stateexample')
def stateExample():
        name = 'State Pattern Example.'
        link = 'examples/stateex.html'
        button = '/state'
        return render_template('tempex.html', yesStateex = 'active', name = name, button = button, link = link)

#STRATEGY

@app.route('/strategy')
def strategy():
        name = 'Strategy Pattern.'

        forces = '''You need to be able to change a class behavior at run time.'''

        solution = '''To do this you need to create objects that represent various
		stratgies as well as create another object that has a varying behaviors
		depending on the stategy object.'''

        related = ['Template Method Pattern.', 'State Pattern.']

        link = '/strategyexample'

        return render_template('template.html', yesStrat = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/strategyexample')
def strategyExample():
        name = 'Strategy Pattern Example.'
        link = 'examples/strategyex.html'
        button = '/strategy'
        return render_template('tempex.html', yesStratex = 'active', name = name, button = button, link = link)

#PROTOTYPE

@app.route('/prototype')
def prototype():
        name = 'Prototype Pattern.'

        forces = '''You want to use an object that us already is your program but you need to change a couple
		details while still keeping the orignal object the same.'''

        solution = '''To achieve this you create a method named "clone". This clone method will have a list
		of cloneable classes. So when you want that object but need to make some changes, you call
		the clone method.'''

        related = ['Singleton Pattern.', 'Template Method Pattern.']

        link = '/prototypeexample'

        return render_template('template.html', yesProto = 'active', name = name, forces = forces, solution = solution, related = related, link = link)

@app.route('/prototypeexample')
def prototypeExample():
        name = 'Prototype Pattern Example.'
        link = 'examples/prototypeex.html'
        button = '/prototype'
        return render_template('tempex.html', yesProtoex = 'active', name = name, button = button, link = link)

if __name__ == '__main__':
	app.run('198.110.204.9', 5000, debug = True)
