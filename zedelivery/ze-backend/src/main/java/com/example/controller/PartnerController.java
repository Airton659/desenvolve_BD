package com.example.controller;

import com.example.model.*;
import com.example.repository.*;
import com.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("/partners")
public class PartnerController {

    @Autowired
    private PartnerRepository partnerRepository;

    @PostMapping
    public Partner createPartner(@RequestBody Partner partner) {
        return partnerRepository.save(partner);
    }

    @GetMapping("/{id}")
    public Partner getPartner(@PathVariable String id) {
        return partnerRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Parceiro não encontrado..."));
    }

    @PostMapping("/search")
    public Partner searchPartner(@RequestBody String location) {
        return partnerRepository.findAll().get(0);
    }
}