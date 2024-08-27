import React, { useState } from 'react';

const DropdownCustom = () => {
  const [selectedOption, setSelectedOption] = useState('');
  const [dependentOptions, setDependentOptions] = useState([]);

  const handleMainDropdownChange = (event) => {
    const selectedValue = event.target.value;
    setSelectedOption(selectedValue);

    // Aqui você pode fazer uma requisição para obter as opções dependentes com base na opção selecionada
    // Neste exemplo, vamos usar um mapeamento simples
    if (selectedValue === 'Saúde') {
      setDependentOptions(['Mortalidade']);
    } else if (selectedValue === 'Educação') {
      setDependentOptions(['Matrícula', 'Rendimento']);
    } else {
      setDependentOptions([]);
    }
  };

  return (
    <div className='flex-col'>
      <select id='contextDropdown' value={selectedOption} onChange={handleMainDropdownChange}>
        <option value="">Selecione uma opção</option>
        <option value="Saúde">Saúde</option>
        <option value="Educação">Educação</option>
        {/* <option value="Option3">Opção 3</option> */}
      </select>
      <br/>
      {dependentOptions.length > 0 && (
        <select className='mt-3' id='opcaoDropdown'>
          {dependentOptions.map((option, index) => (
            <option key={index} value={option}>
              {option}
            </option>
          ))}
        </select>
      )}
    </div>
  );
};

export default DropdownCustom;
