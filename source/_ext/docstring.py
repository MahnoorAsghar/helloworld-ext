from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.core import publish_doctree
import docutils
from docutils.parsers.rst import Parser
from docutils.utils import new_document
import docutils.parsers.rst.states
import re
import os
import yaml
from yaml.loader import SafeLoader



class yamlParse:
    def readFromFile(fpath):
        with open(fpath, 'r') as stream:
            yamlData = yaml.load(stream, Loader=yaml.SafeLoader)
            return yamlData 


class Parameters(Directive):
    required_arguments = 1
    has_content = True

    def run(self):
        print(f'Parameters.run called')

        #Parse the input field list from the docstring
        regexPattern = "((^:{1}.*:{1})(.*))"
        fieldList = {} #dict to hold parsed input field list
        
        for c in self.content:
            regexOutput = re.match(regexPattern, c)

            field = regexOutput.groups()
            fieldName = field[1].strip(':')
            fieldBody = field[2].strip()

            fieldList[fieldName] = fieldBody
                
        #read from yaml file
        paramFile = self.arguments[0] 
        curPath = os.path.dirname( os.path.dirname(os.path.abspath(__file__)) )       
        paramFilePath = curPath + '/' + paramFile
        yamlData = yamlParse.readFromFile(paramFilePath)
        
        fieldListNode = nodes.field_list()
        
        #Substitute the descriptions
        for fieldName in fieldList:
            if fieldName in yamlData.keys():
                fieldList[fieldName] = yamlData[fieldName]["description"]
            
            fNamePara = nodes.Text(data = fieldName)
            fBodyPara = nodes.Text(data = fieldList[fieldName])
            print(f'fNamePara: {type(fNamePara)}\n{fNamePara}\n\n')
        
        
            fieldNameNode = nodes.field_name()
            fieldNameNode.setup_child(fNamePara)
            fieldNameNode.children.append(fNamePara)
            print(f'fieldNameNode: {fieldNameNode}\n')
                #f'dir(fieldNameNode): {dir(fieldNameNode)}\n\n')
       
            fBodyNode = nodes.field_body()
            fBodyNode.setup_child(fBodyPara)
            fBodyNode.children.append(fBodyPara)
       
            fieldNode = nodes.field()
            fieldNode.setup_child(fieldNameNode)
            fieldNode.setup_child(fBodyNode)
            fieldNode.children.append(fieldNameNode)
            fieldNode.children.append(fBodyNode)

            fieldListNode.setup_child(fieldNode)
            fieldListNode.children.append(fieldNode)
        
        print(f'fieldListNode: {fieldListNode}\n') 
      
        return [fieldListNode]

        #paragraph_node = nodes.paragraph(text='Hello World')
        #print(f'paragraph_node: {paragraph_node}')
        #return [paragraph_node]



def setup(app):
    print('Setting up docstring extension...\n')
    app.add_directive("parameters", Parameters)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
            }

    yamlParser = yamlParser()
    yamlParser.readFromFile('parameters.yaml')
